import unittest
from unittest.mock import MagicMock

from app.classes.selection.all_nodes import *
from app.classes.spec.domain_object import DomainEvent, DomainProp
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.custom_event.custom_event import CustomEvent, ConjType 
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.verb import Verb, VerbConjugations, VerbType
from app.classes.custom_event.prep_phrase import PrepPhrase

from app.src.sym_updaters.custom_event.asset_type_extractor import AssetTypeExtractor
from app.src.sym_updaters.custom_event.event_declaration_mapper import EventDeclarationMapper
from app.src.sym_updaters.custom_event.declaration_prop_mapper import DeclarationPropMapper

from tests.nlp.test_objects import CustomEvents

test_set = [
    (
        CustomEvents.legal_proceedings(),
        Declaration('evt_legal_proceedings_necessary', 'LegalProceedingsNecessary', 'events', [])
    ),
    (
        CustomEvents.paying(),
        Declaration('evt_pay', 'Pay', 'events', [
            DeclarationProp('paying_agent', 'buyer', 'Role'),
            DeclarationProp('paying_target', 'seller', 'Role'),
            DeclarationProp('pay_object', '$100', 'Amount'), 
            DeclarationProp('pay_method', 'credit card', 'String'), 
        ])
    ),
    (
        CustomEvents.eating_pie(),
        Declaration('evt_eat_noisily', 'EatNoisily', 'events', [
            DeclarationProp('eating_agent', 'Bob', 'Role'),
            DeclarationProp('eating_target', 'seller', 'Role'), # Doesnt really make sense
            DeclarationProp('eat_object', 'apple pie', 'String'), 
        ])
    ),
    (
        CustomEvent(
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


class CustomEventTests(unittest.TestCase):
    def setUp(self) -> None:
        asset_type_extractor = AssetTypeExtractor()
        prop_mapper = DeclarationPropMapper(asset_type_extractor)
        self.sut = EventDeclarationMapper(prop_mapper)

    def test_custom_event_mapping(self):
        for evt, expected_obj in test_set:
            result = self.sut.map(evt)
            self.assertEqual(result, expected_obj)

    
if __name__ == '__main__':
    unittest.main()