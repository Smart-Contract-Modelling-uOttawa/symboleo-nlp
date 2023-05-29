import unittest
from app.templates.template_getter import get_template

from app.src.helpers.declarer import Declarer

class DeclarerTests(unittest.TestCase):

    @unittest.skip('todo')
    def test_declarer(self):
        contract = get_template('sample_raw')
        expected_value = 'evt_delivered: Delivered with item := goods, deliveryAddress := 123 main street, delDueDate := 2023/04/25;'
    
        # Delivered isAn Event with item: Meat, deliveryAddress: String, delDueDate: Date;
        decl = Declarer.declare(contract.domain_model, 'events', 'Delivered', 'evt_delivered', [
            ('item', 'goods'),
            ('deliveryAddress', '123 main street'),
            ('delDueDate', '2023/04/25')
        ])

        self.assertEqual(decl.to_sym(), expected_value)

    @unittest.skip('todo')
    def test_declarer_error(self):
        contract = get_template('sample_raw')

        with self.assertRaises(Exception) as context:
            Declarer.declare(contract.domain_model, 'events', 'Delivered', 'evt_delivered', [
            ('XXX', 'goods')
        ])
        
        self.assertTrue('property XXX not found' in str(context.exception))
        # Delivered isAn Event with item: Meat, deliveryAddress: String, delDueDate: Date;
        
    

if __name__ == '__main__':
    unittest.main()
    