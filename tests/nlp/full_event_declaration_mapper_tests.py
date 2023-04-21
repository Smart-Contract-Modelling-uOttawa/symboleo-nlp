import unittest
from unittest.mock import MagicMock

from app.classes.selection.all_nodes import *
from app.classes.spec.domain_object import DomainEvent, DomainProp
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.other.frame_event import FrameEvent, ConjType 
from app.classes.other.noun_phrase import NounPhrase
from app.classes.other.verb import Verb, VerbConjugations, VerbType
from app.classes.other.prep_phrase import PrepPhrase

from app.src.nlp.frame_event.asset_type_extractor import AssetTypeExtractor
from app.src.nlp.frame_event.event_declaration_mapper import EventDeclarationMapper
from app.src.nlp.frame_event.declaration_prop_mapper import DeclarationPropMapper

from tests.nlp.test_objects import FrameEvents

test_set = [
    (
        FrameEvents.legal_proceedings(),
        Declaration('evt_legal_proceedings_necessary', 'LegalProceedingsNecessary', 'events', [])
    ),
    (
        FrameEvents.paying(),
        Declaration('evt_pay', 'Pay', 'events', [
            DeclarationProp('paying_agent', 'buyer', 'Role'),
            DeclarationProp('paying_target', 'seller', 'Role'),
            DeclarationProp('pay_object', '$100', 'Amount'), 
            DeclarationProp('pay_method', 'credit card', 'String'), 
        ])
    ),
    (
        FrameEvents.eating_pie(),
        Declaration('evt_eat_noisily', 'EatNoisily', 'events', [
            DeclarationProp('eating_agent', 'Bob', 'Role'),
            DeclarationProp('eating_target', 'seller', 'Role'), # Doesnt really make sense
            DeclarationProp('eat_object', 'apple pie', 'String'), 
        ])
    ),
    (
        FrameEvent(
            subj = NounPhrase('The renter', 'renter', is_role=True),
            verb = Verb('occupies', 'occupy', [VerbType.TRANSITIVE], VerbConjugations('occupy', 'occupies', 'occupied', 'occupying')),
            dobj = NounPhrase('the property', 'property')
        ),
        Declaration('evt_occupy', 'Occupy', 'events', [
            DeclarationProp('occupying_agent', 'renter', 'Role'),
            DeclarationProp('occupy_object', 'property', 'String') # This should be logged as an asset... need to inject it though
        ])
    )
]


class FrameEventTests(unittest.TestCase):
    def setUp(self) -> None:
        asset_type_extractor = AssetTypeExtractor()
        prop_mapper = DeclarationPropMapper(asset_type_extractor)
        self.sut = EventDeclarationMapper(prop_mapper)

    def test_frame_event_mapping(self):
        for frame_event, expected_obj in test_set:
            result = self.sut.map(frame_event)
            self.assertEqual(result, expected_obj)

    
if __name__ == '__main__':
    unittest.main()