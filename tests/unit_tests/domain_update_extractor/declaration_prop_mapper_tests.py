import unittest
from unittest.mock import MagicMock

from app.classes.spec.declaration import DeclarationProp
from app.src.domain_update_extractor.declaration_prop_mapper import DeclarationPropMapper
from tests.helpers.test_objects import CustomEvents

class DeclarationPropMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = DeclarationPropMapper()

    def test_declaration_prop_mapper_subject_role(self):
        evt = CustomEvents.paying()

        exp_subj_prop = DeclarationProp('paying_agent', 'buyer', 'Role')
        subj_result = self.sut.map_subject(evt.subj, evt)

        self.assertEqual(subj_result, exp_subj_prop)
    

    def test_declaration_prop_mapper_subject_not_role(self):
        evt = CustomEvents.legal_proceedings()

        exp_prop = DeclarationProp('becoming_subject', 'legal_proceedings', 'Proceedings')
        result = self.sut.map_subject(evt.subj, evt)

        self.assertEqual(result, exp_prop)


    def test_declaration_prop_mapper_dobject(self):
        evt = CustomEvents.paying()

        exp_prop = DeclarationProp('paid_object', '100', 'Money') 
        result = self.sut.map_dobject(evt.dobj, evt)

        self.assertEqual(result, exp_prop)


    def test_declaration_prop_mapper_dobject_contract(self):
        evt = CustomEvents.contract_dobj()

        result = self.sut.map_dobject(evt.dobj, evt)

        self.assertIsNone(result)
    
    def test_declaration_prop_mapper_dobject_parm(self):
        evt = CustomEvents.eating_parm()

        exp_prop = DeclarationProp('test_value', '[TEST_VALUE]', 'String') 
        result = self.sut.map_dobject(evt.dobj, evt)

        self.assertEqual(result, exp_prop)
    

    def test_declaration_prop_mapper_dobject_role(self):
        evt = CustomEvents.disrupt_buyer()

        exp_prop = DeclarationProp('disrupted_target', 'buyer', 'Role') 
        result = self.sut.map_dobject(evt.dobj, evt)

        self.assertEqual(result, exp_prop)
    

    def test_declaration_prop_mapper_pp1(self):
        evt = CustomEvents.paying()

        exp_res = DeclarationProp('paying_target', 'seller', 'Role') 
        result = self.sut.map_prep_phrase(evt.pps[0], evt)

        self.assertEqual(result, exp_res)
    

    def test_declaration_prop_mapper_pp2(self):
        evt = CustomEvents.paying()

        exp_res = DeclarationProp('pay_method', 'credit card', 'PaymentMethod') 
        result = self.sut.map_prep_phrase(evt.pps[1], evt)

        self.assertEqual(result, exp_res)
    

    def test_declaration_prop_mapper_pp3(self):
        evt = CustomEvents.eating_pie()

        exp_res = DeclarationProp('eating_co_agent', 'seller', 'Role') 
        result = self.sut.map_prep_phrase(evt.pps[0], evt)

        self.assertEqual(result, exp_res)
    

    def test_declaration_prop_mapper_pp4(self):
        evt = CustomEvents.provide_authorization()

        exp_res = DeclarationProp('provide_detail', 'pets', 'Pets') 
        result = self.sut.map_prep_phrase(evt.pps[0], evt)

        self.assertEqual(result, exp_res)


    def test_declaration_prop_mapper_pp5(self):
        evt = CustomEvents.disrupt_buyer()

        exp_res = DeclarationProp('disrupt_detail', 'the phone', 'Phone') 
        result = self.sut.map_prep_phrase(evt.pps[0], evt)

        self.assertEqual(result, exp_res)

if __name__ == '__main__':
    unittest.main()