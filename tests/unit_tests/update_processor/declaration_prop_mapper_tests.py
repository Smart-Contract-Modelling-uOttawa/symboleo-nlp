import unittest
from unittest.mock import MagicMock

from app.classes.spec.declaration import DeclarationProp
from app.src.update_processor.declaration_prop_mapper import DeclarationPropMapper
from tests.helpers.test_objects import CustomEvents

# TODO: Should make a test suite, and/or break up the class

class DeclarationPropMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = DeclarationPropMapper()

    def test_declaration_prop_mapper_subject(self):
        evt = CustomEvents.paying()

        exp_subj_prop = DeclarationProp('paying_agent', 'buyer', 'Role')
        subj_result = self.sut.map_subject(evt.subj, evt)

        self.assertEqual(subj_result, exp_subj_prop)

    
    def test_declaration_prop_mapper_dobject(self):
        evt = CustomEvents.paying()

        exp_res = DeclarationProp('paid_object', '100', 'Money') 
        result = self.sut.map_dobject(evt.dobj, evt)

        self.assertEqual(result, exp_res)
    

    def test_declaration_prop_mapper_pp1(self):
        evt = CustomEvents.paying()

        exp_res = DeclarationProp('paying_target', 'the seller', 'Role') 
        result = self.sut.map_prep_phrase(evt.pps[0], evt)

        self.assertEqual(result, exp_res)
    

    def test_declaration_prop_mapper_pp2(self):
        evt = CustomEvents.paying()

        exp_res = DeclarationProp('pay_method', 'credit card', 'PaymentMethod') 
        result = self.sut.map_prep_phrase(evt.pps[1], evt)

        self.assertEqual(result, exp_res)

if __name__ == '__main__':
    unittest.main()