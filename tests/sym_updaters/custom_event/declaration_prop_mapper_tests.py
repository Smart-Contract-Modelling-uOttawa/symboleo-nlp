import unittest
from unittest.mock import MagicMock

from app.classes.custom_event.noun_phrase import NounPhrase


from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.domain_object import Asset, DomainEvent, DomainProp

from app.src.sym_updaters.custom_event.declaration_prop_mapper import DeclarationPropMapper
from app.src.sym_updaters.custom_event.asset_type_extractor import IExtractAssetType

from tests.helpers.test_objects import CustomEvents

class DeclarationPropMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.type_extractor = IExtractAssetType()
        self.sut = DeclarationPropMapper(self.type_extractor)

    def test_declaration_prop_mapper_subject(self):
        evt = CustomEvents.paying()
        self.type_extractor.extract = MagicMock(return_value = None)

        exp_subj_prop = DeclarationProp('paying_agent', 'buyer', 'Role')
        subj_result = self.sut.map_subject(evt.subj, evt, [])

        self.assertEqual(subj_result, exp_subj_prop)
        self.assertEqual(self.type_extractor.extract.call_count, 0)

    
    def test_declaration_prop_mapper_dobject(self):
        evt = CustomEvents.paying()
        self.type_extractor.extract = MagicMock(return_value = 'Amount')

        # This should be an amount, which may be another asset
        exp_dobj_prop = DeclarationProp('pay_object', '$100', 'Amount') 
        dobj_result = self.sut.map_dobject(evt.dobj, evt, [])

        self.assertEqual(dobj_result, exp_dobj_prop)
        self.assertEqual(self.type_extractor.extract.call_count, 1)
    

    def test_declaration_prop_mapper_pp1(self):
        evt = CustomEvents.paying()
        self.type_extractor.extract = MagicMock(return_value = None)

        # This should be an amount, which may be another asset
        exp = DeclarationProp('paying_target', 'seller', 'Role') 
        result = self.sut.map_prep_phrase(evt.pps[0], evt, [])

        self.assertEqual(result, exp)
        self.assertEqual(self.type_extractor.extract.call_count, 0)
    

    def test_declaration_prop_mapper_pp2(self):
        evt = CustomEvents.paying()
        self.type_extractor.extract = MagicMock(return_value = 'Method')

        # This should be an amount, which may be another asset
        exp = DeclarationProp('pay_method', 'credit card', 'Method') 
        result = self.sut.map_prep_phrase(evt.pps[1], evt, [])

        self.assertEqual(result, exp)
        self.assertEqual(self.type_extractor.extract.call_count, 1)

if __name__ == '__main__':
    unittest.main()