"""Offline regressions for the published 1.2.0 confirmation generator.

Run in Compose with Node and PyYAML. Uses only synthetic/public example data.
No network request, signed replay or certification result is produced.
"""
import base64
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1] / 'config/flows/Logistics (NIC2004:60232)'
FLOWS = ('ORDER_FLOW_BASELINE.yaml', 'BUYER_SIDE_ORDER_CANCELLATION.yaml',
         'ORDER_FLOW_BASELINE_without_rts_.yaml')
NODE = r'''
const fs = require('node:fs');
const vm = require('node:vm');
const data = JSON.parse(fs.readFileSync(0, 'utf8'));
const sandbox = { console: { log() {}, error() {}, warn() {} } };
vm.createContext(sandbox);
vm.runInContext(data.helper + '\n' + data.generator, sandbox, { timeout: 1000 });
(async () => {
 const output = await sandbox.generate(data.payload, data.session);
 const snapshot = JSON.parse(JSON.stringify(output));
 if (data.probeMutation) {
   output.message.order.tags[0].list[0].value = 'modified by caller';
   for (const leg of output.message.order.fulfillments) {
     for (const endpoint of ['start','end']) {
       if (leg[endpoint]?.contact) leg[endpoint].contact.phone = 'changed';
     }
   }
 }
 process.stdout.write(JSON.stringify({output:snapshot, session:data.session}));
})().catch(error => { console.error(error.stack); process.exitCode=1; });
'''


def fixture(name, omit_contact=False):
    flow = json.loads(json.dumps(yaml.safe_load((ROOT / name).read_text()), default=lambda value: value.isoformat()))
    steps = {s['api']: s['mock'] for s in flow['steps']}
    confirm = deepcopy(steps['confirm']['defaultPayload'])
    reviewed = deepcopy(steps['init']['defaultPayload']['message']['order'])
    reviewed.update(deepcopy(steps['on_init']['defaultPayload']['message']['order']))
    search = steps['search']['defaultPayload']['message']['intent']
    provider = steps['on_search']['defaultPayload']['message']['catalog']['bpp/providers'][0]
    terms = [{'code':'bpp_terms','list':[
        {'code':'static_terms','value':'https://seller.example.test/accepted-terms'},
        {'code':'max_liability','value':'7'},
        {'code':'max_liability_cap','value':'25000'},
    ]}]
    reviewed['tags'] = terms
    for index, leg in enumerate(reviewed['fulfillments']):
        for endpoint in ('start','end'):
            leg[endpoint]['contact'] = {
                'phone':f'00000000{index}{0 if endpoint == "start" else 1}',
                'email':f'{endpoint}{index}@seller.example.test',
            }
            if omit_contact:
                leg[endpoint].pop('contact')
    session = {
        'city_code':['std:080'], 'provider_id':[reviewed['provider']['id']],
        'items':[deepcopy(reviewed['items'])], 'billing':[deepcopy(reviewed['billing'])],
        'on_search_items':[deepcopy(provider['items'])],
        'on_search_fulfillments':[deepcopy(provider['fulfillments'])],
        'init_fulfillments':[deepcopy(reviewed['fulfillments'])],
        'on_init_start_location':[deepcopy(reviewed['fulfillments'][0]['start']['location'])],
        'on_init_end_location':[deepcopy(reviewed['fulfillments'][0]['end']['location'])],
        'quote':[deepcopy(reviewed['quote'])], 'payment':[deepcopy(reviewed['payment'])],
        'cancellation_terms':[deepcopy(reviewed.get('cancellation_terms',[]))],
        'payload_details':[deepcopy(search['@ondc/org/payload_details'])],
        'retail_category':[search['@ondc/org/payload_details']['category']],
        'category_id':search['category']['id'], 'payment_type':'PRE-FULFILLMENT',
        'user_inputs':{'returnToOrigin':'no'},
        'on_init_order_tags':[deepcopy(terms)],
        'on_init_fulfillments':[deepcopy(reviewed['fulfillments'])],
    }
    data = {'helper':base64.b64decode(flow['helperLib']).decode(),
            'generator':base64.b64decode(steps['confirm']['generate']).decode(),
            'payload':confirm,'session':session}
    return steps, reviewed, data


def generate(data):
    run = subprocess.run(['node','-e',NODE], input=json.dumps(data), text=True,
                         capture_output=True, timeout=15)
    if run.returncode:
        raise AssertionError(run.stderr)
    return json.loads(run.stdout)


class ConfirmAgreement(unittest.TestCase):
    def test_on_init_saves_the_reviewed_terms_and_fulfillments(self):
        for name in FLOWS:
            with self.subTest(flow=name):
                steps, _, _ = fixture(name)
                self.assertEqual(steps['on_init']['saveData'].get('on_init_order_tags'),
                                 '$.message.order.tags')
                self.assertEqual(steps['on_init']['saveData'].get('on_init_fulfillments'),
                                 '$.message.order.fulfillments')

    def test_confirm_preserves_seller_terms_and_buyer_acknowledgement(self):
        for name in FLOWS:
            with self.subTest(flow=name):
                _, reviewed, data = fixture(name)
                order = generate(data)['output']['message']['order']
                seller = [t for t in order['tags'] if t['code']=='bpp_terms']
                self.assertEqual(seller, reviewed['tags'])
                buyer = [t for t in order['tags'] if t['code']=='bap_terms']
                self.assertEqual(len(buyer),1)
                self.assertIn({'code':'accept_bpp_terms','value':'Y'}, buyer[0]['list'])

    def test_confirm_preserves_both_reviewed_contacts(self):
        for name in FLOWS:
            with self.subTest(flow=name):
                _, reviewed, data = fixture(name)
                order = generate(data)['output']['message']['order']
                for leg in order['fulfillments']:
                    prior = next(x for x in reviewed['fulfillments'] if x['id']==leg['id'])
                    for endpoint in ('start','end'):
                        self.assertEqual(leg[endpoint]['contact'],prior[endpoint]['contact'])

    def test_new_session_data_is_not_mutated(self):
        for name in FLOWS:
            with self.subTest(flow=name):
                _, _, data = fixture(name)
                before = deepcopy(data['session'])
                data['probeMutation'] = True
                after = generate(data)['session']
                for key in ('on_init_order_tags','on_init_fulfillments'):
                    self.assertEqual(after[key],before[key])

    def test_missing_reviewed_contact_preserves_the_buyers_default(self):
        for name in FLOWS:
            with self.subTest(flow=name):
                _, _, data = fixture(name,omit_contact=True)
                default = deepcopy(data['payload']['message']['order']['fulfillments'])
                order = generate(data)['output']['message']['order']
                for leg, original in zip(order['fulfillments'],default):
                    for endpoint in ('start','end'):
                        self.assertEqual(leg[endpoint].get('contact'),original[endpoint].get('contact'))


    def test_contacts_are_not_copied_from_another_fulfillment(self):
        for name in FLOWS:
            with self.subTest(flow=name):
                _, _, data = fixture(name)
                default = deepcopy(data['payload']['message']['order']['fulfillments'])
                for leg in data['session']['on_init_fulfillments'][0]:
                    leg['id'] = 'different-fulfillment'
                order = generate(data)['output']['message']['order']
                for leg, original in zip(order['fulfillments'],default):
                    for endpoint in ('start','end'):
                        self.assertEqual(leg[endpoint].get('contact'),original[endpoint].get('contact'))

    def test_reviewed_quote_payment_and_locations_are_preserved(self):
        for name in FLOWS:
            with self.subTest(flow=name):
                _, _, data = fixture(name)
                expected = deepcopy(data['session'])
                order = generate(data)['output']['message']['order']
                quote = expected['quote'][0]
                quote.pop('ttl',None)
                self.assertEqual(order['quote'],quote)
                self.assertEqual(order['payment'],expected['payment'][0])
                self.assertEqual(order['fulfillments'][0]['start']['location'],expected['on_init_start_location'][0])
                self.assertEqual(order['fulfillments'][0]['end']['location'],expected['on_init_end_location'][0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
