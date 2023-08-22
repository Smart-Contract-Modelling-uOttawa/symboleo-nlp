import unittest
from unittest.mock import MagicMock

from app.classes.spec.declaration import Declaration, DeclarationProp, EventDeclaration

from app.src.domain_update_extractor.event_declaration_mapper import EventDeclarationMapper
from app.src.domain_update_extractor.declaration_prop_mapper import IMapDeclarationProps

from tests.helpers.test_objects import CustomEvents

class EventDeclarationMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.prop_mapper = IMapDeclarationProps()
        self.sut = EventDeclarationMapper(self.prop_mapper)


    def test_evt_decl_mapping_linking(self):
        evt = CustomEvents.legal_proceedings_det()

        evt.get_declaration_name = MagicMock(return_value='decl_name')
        evt.event_key = MagicMock(return_value='event_key')

        sp = DeclarationProp('sk', 'sv', 'st')
        dp = DeclarationProp('dk', 'dv', 'dt')
        pp1 = DeclarationProp('pk1', 'pv1', 'pt1')
        pp2 = DeclarationProp('pk2', 'pv2', 'pt2')
        self.prop_mapper.map_subject = MagicMock(return_value = sp)
        self.prop_mapper.map_dobject = MagicMock(return_value = dp)
        self.prop_mapper.map_prep_phrase = MagicMock(side_effect = [pp1,pp2])

        exp = EventDeclaration('event_key', 'decl_name', [
            pp1, pp2
        ])

        result = self.sut.map(evt)

        self.assertEqual(result, exp)
        self.assertEqual(self.prop_mapper.map_subject.call_count, 0)
        self.assertEqual(self.prop_mapper.map_dobject.call_count, 0)
        self.assertEqual(self.prop_mapper.map_prep_phrase.call_count, 2)
    
    def test_evt_decl_mapping_linking_role(self):
        evt = CustomEvents.bob_happy()
        evt.get_declaration_name = MagicMock(return_value='decl_name')
        evt.event_key = MagicMock(return_value='event_key')

        sp = DeclarationProp('agent', 'Bob', 'Role')
        exp = EventDeclaration('event_key', 'decl_name', [sp])

        result = self.sut.map(evt)
        self.assertEqual(result, exp)
    

    def test_evt_decl_mapping_intransitive(self):
        evt = CustomEvents.bob_complies()

        evt.get_declaration_name = MagicMock(return_value='decl_name')
        evt.event_key = MagicMock(return_value='event_key')

        sp = DeclarationProp('sk', 'sv', 'st')
        pp1 = DeclarationProp('pk1', 'pv1', 'pt1')
        self.prop_mapper.map_subject = MagicMock(return_value = sp)

        exp = EventDeclaration('event_key', 'decl_name', [
            sp
        ])

        result = self.sut.map(evt)

        self.assertEqual(result, exp)
        self.assertEqual(self.prop_mapper.map_subject.call_count, 1)
    

    def test_evt_decl_transitive(self):
        evt = CustomEvents.paying()
        evt.get_declaration_name = MagicMock(return_value='decl_name')
        evt.event_key = MagicMock(return_value='event_key')

        sp = DeclarationProp('sk', 'sv', 'st')
        dp = DeclarationProp('dk', 'dv', 'dt')
        pp1 = DeclarationProp('pk1', 'pv1', 'pt1')
        pp2 = DeclarationProp('pk2', 'pv2', 'pt2')
        self.prop_mapper.map_subject = MagicMock(return_value = sp)
        self.prop_mapper.map_dobject = MagicMock(return_value = dp)
        self.prop_mapper.map_prep_phrase = MagicMock(side_effect = [pp1,pp2])

        exp = EventDeclaration('event_key', 'decl_name', [
            sp, dp, pp1, pp2
        ])

        result = self.sut.map(evt)

        self.assertEqual(result, exp)
        self.assertEqual(self.prop_mapper.map_subject.call_count, 1)
        self.assertEqual(self.prop_mapper.map_dobject.call_count, 1)
        self.assertEqual(self.prop_mapper.map_prep_phrase.call_count, 2)
    

if __name__ == '__main__':
    unittest.main()