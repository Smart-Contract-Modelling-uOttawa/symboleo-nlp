import unittest
from app.src.helpers.template_getter import get_template

class ToSymTests(unittest.TestCase):

    def test_to_sym(self):
        contract = get_template('sample_raw')
        result = contract.to_sym()

        with open('tests/symboleo_spec/sample_target.txt', 'r') as f:
            expected = f.read()

        self.assertEqual(result, expected)
    

if __name__ == '__main__':
    unittest.main()