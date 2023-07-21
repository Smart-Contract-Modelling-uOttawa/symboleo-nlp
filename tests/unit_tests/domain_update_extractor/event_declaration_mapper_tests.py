import unittest
from unittest.mock import MagicMock

from app.classes.spec.declaration import Declaration, DeclarationProp

from app.src.domain_update_extractor.event_declaration_mapper import EventDeclarationMapper
from app.src.domain_update_extractor.declaration_prop_mapper import IMapDeclarationProps

from tests.helpers.test_objects import CustomEvents

class CustomEventTests(unittest.TestCase):
    def setUp(self) -> None:
        self.prop_mapper = IMapDeclarationProps()
        self.sut = EventDeclarationMapper(self.prop_mapper)

    @unittest.skip('fix')
    def test_evt_decl_mapping_linking(self):
        evt = CustomEvents.legal_proceedings_det()

        sp = DeclarationProp('sk', 'sv', 'st')
        dp = DeclarationProp('dk', 'dv', 'dt')
        pp1 = DeclarationProp('pk1', 'pv1', 'pt1')
        pp2 = DeclarationProp('pk2', 'pv2', 'pt2')
        self.prop_mapper.map_subject = MagicMock(return_value = sp)
        self.prop_mapper.map_dobject = MagicMock(return_value = dp)
        self.prop_mapper.map_prep_phrase = MagicMock(side_effect = [pp1,pp2])

        exp = Declaration('evt_legal_proceedings_necessary', 'LegalProceedingsNecessary', 'events', [
            pp1, pp2
        ])

        result = self.sut.map(evt)
    
        self.assertEqual(result, exp)
        self.assertEqual(self.prop_mapper.map_subject.call_count, 0)
        self.assertEqual(self.prop_mapper.map_dobject.call_count, 0)
        self.assertEqual(self.prop_mapper.map_prep_phrase.call_count, 2)
    
    @unittest.skip('fix')
    def test_evt_decl_transitive(self):
        evt = CustomEvents.paying()

        sp = DeclarationProp('sk', 'sv', 'st')
        dp = DeclarationProp('dk', 'dv', 'dt')
        pp1 = DeclarationProp('pk1', 'pv1', 'pt1')
        pp2 = DeclarationProp('pk2', 'pv2', 'pt2')
        self.prop_mapper.map_subject = MagicMock(return_value = sp)
        self.prop_mapper.map_dobject = MagicMock(return_value = dp)
        self.prop_mapper.map_prep_phrase = MagicMock(side_effect = [pp1,pp2])

        exp = Declaration('evt_pay', 'Pay', 'events', [
            sp, dp, pp1, pp2
        ])

        result = self.sut.map(evt)
    
        self.assertEqual(result, exp)
        self.assertEqual(self.prop_mapper.map_subject.call_count, 1)
        self.assertEqual(self.prop_mapper.map_dobject.call_count, 1)
        self.assertEqual(self.prop_mapper.map_prep_phrase.call_count, 2)
    

if __name__ == '__main__':
    unittest.main()