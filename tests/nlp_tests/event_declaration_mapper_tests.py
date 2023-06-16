import unittest
from unittest.mock import MagicMock

from app.classes.elements.all_elements import *
from app.classes.spec.declaration import Declaration, DeclarationProp

from app.src.domain_update_extractor.event_declaration_mapper import EventDeclarationMapper
from app.src.domain_update_extractor.declaration_prop_mapper import DeclarationPropMapper


from tests.helpers.test_objects import CustomEvents

test_suite = [
    (
        CustomEvents.occupy_property(),
        Declaration('evt_occupy', 'Occupy', 'events', [
            DeclarationProp('occupying_agent', 'renter', 'Role'),
            DeclarationProp('occupied_object', 'property', 'RentalProperty'),
        ])
    ),

    (
        CustomEvents.abandon_property(),
        Declaration('evt_abandon', 'Abandon', 'events', [
            DeclarationProp('abandonning_agent', 'renter', 'Role'),
            DeclarationProp('abandonned_object', 'property', 'RentalProperty'),
        ])
    ),

    (
        CustomEvents.legal_proceedings(),
        Declaration('evt_legal_proceedings_necessary', 'LegalProceedingsNecessary', 'events', [
        ])
    ),

    (
        CustomEvents.eating_pie(),
        Declaration('evt_eat_noisily', 'EatNoisily', 'events', [
            DeclarationProp('eating_agent', 'Bob', 'Role'),
            DeclarationProp('ate_object', 'apple_pie', 'Pie'),
            DeclarationProp('eating_co_agent', 'the seller', 'Role'),
        ])
    ),

    (
        CustomEvents.paying(),
        Declaration('evt_pay', 'Pay', 'events', [
            DeclarationProp('paying_agent', 'buyer', 'Role'),
            DeclarationProp('paid_object', '100', 'Money'), 
            DeclarationProp('paying_target', 'the seller', 'Role'), 
            DeclarationProp('pay_method', 'credit card', 'PaymentMethod'),
        ])
    )
]

class EventDeclarationMapperFullTests(unittest.TestCase):
    def setUp(self) -> None:
        # Will prob need to add deps...
        prop_mapper = DeclarationPropMapper()
        self.sut = EventDeclarationMapper(prop_mapper)

    @unittest.skip('fix')
    def test_event_declaration_mapping(self):
        for evt, exp_res in test_suite:
            res = self.sut.map(evt)

            # res.print_me()
            # exp_res.print_me()

            self.assertEqual(exp_res, res )
    

if __name__ == '__main__':
    unittest.main()