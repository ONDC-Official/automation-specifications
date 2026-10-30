"""Execute public logistics mock generators; no network or signed replay."""
import base64
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1] / 'config/flows/Logistics (NIC2004:60232)'
FLOWS = sorted(ROOT.glob('*.yaml'))
NODE = r'''
const fs = require('node:fs');
const vm = require('node:vm');
const data = JSON.parse(fs.readFileSync(0, 'utf8'));
const sandbox = {console: {log() {}, error() {}, warn() {}}};
vm.createContext(sandbox);
vm.runInContext(data.helper + '\n' + data.generator, sandbox, {timeout: 1000});
Promise.resolve(sandbox.generate(data.payload, {user_inputs: data.inputs}))
 .then(output => process.stdout.write(JSON.stringify(output)))
 .catch(error => {console.error(error.stack); process.exitCode = 1;});
'''


def fixture(path):
    flow = yaml.safe_load(path.read_text())
    mock = next(step['mock'] for step in flow['steps'] if step['api'] == 'search')
    properties = mock['inputs']['jsonSchema']['properties']
    return {
        'helper': base64.b64decode(flow['helperLib']).decode(),
        'generator': base64.b64decode(mock['generate']).decode(),
        'payload': deepcopy(mock['defaultPayload']),
        'inputs': {key: value['default'] for key, value in properties.items()
                   if 'default' in value},
    }


def generate(data):
    run = subprocess.run(['node', '-e', NODE], input=json.dumps(
        data, default=lambda value: value.isoformat()), text=True,
        capture_output=True, timeout=15)
    if run.returncode:
        raise AssertionError(run.stderr)
    return json.loads(run.stdout)['message']['intent']


class SearchDefaults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if len(FLOWS) != 5:
            raise AssertionError('Expected all five logistics 1.2.0 flow fixtures')

    def test_default_generated_gps_matches_report_precision(self):
        for path in FLOWS:
            with self.subTest(flow=path.name):
                data = fixture(path)
                intent = generate(data)
                for endpoint in ('start', 'end'):
                    gps = intent['fulfillment'][endpoint]['location']['gps']
                    self.assertRegex(gps, r'^-?\d{1,3}\.\d{6}, ?-?\d{1,3}\.\d{6}$')
                    self.assertEqual([float(x) for x in gps.split(',')],
                                     [12.4535, 77.9283])

    def test_default_synthetic_cargo_explicitly_declares_non_dangerous(self):
        for path in FLOWS:
            with self.subTest(flow=path.name):
                details = generate(fixture(path))['@ondc/org/payload_details']
                self.assertIs(details.get('dangerous_goods'), False)

    def test_custom_coordinates_and_explicit_cargo_flag_are_preserved(self):
        for path in FLOWS:
            with self.subTest(flow=path.name):
                data = fixture(path)
                data['inputs'].update(start_gps='12.5001,77.6002',
                                      end_gps='12.7003,77.8004')
                data['payload']['message']['intent']['@ondc/org/payload_details']['dangerous_goods'] = True
                intent = generate(data)
                for endpoint in ('start', 'end'):
                    self.assertEqual(intent['fulfillment'][endpoint]['location']['gps'],
                                     data['inputs'][endpoint + '_gps'])
                self.assertIs(intent['@ondc/org/payload_details']['dangerous_goods'], True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
