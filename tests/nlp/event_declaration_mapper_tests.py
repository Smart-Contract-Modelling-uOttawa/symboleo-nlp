import unittest
from unittest.mock import MagicMock

from app.classes.selection.all_nodes import *
from app.classes.spec.domain_object import DomainEvent, DomainProp
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.other.frame_event import FrameEvent, ConjType 
from app.classes.other.noun_phrase import NounPhrase
from app.classes.other.verb import Verb, VerbConjugations, VerbType
from app.classes.other.prep_phrase import PrepPhrase

from app.src.nlp.frame_event.event_declaration_mapper import EventDeclarationMapper
from app.src.nlp.frame_event.declaration_prop_mapper import IMapDeclarationProps

from tests.nlp.test_objects import FrameEvents

class FrameEventTests(unittest.TestCase):
    def setUp(self) -> None:
        self.prop_mapper = IMapDeclarationProps()
        self.sut = EventDeclarationMapper(self.prop_mapper)


    def test_evt_decl_mapping_linking(self):
        evt = FrameEvents.legal_proceedings_det()

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
    
    
    def test_evt_decl_transitive(self):
        evt = FrameEvents.paying()

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