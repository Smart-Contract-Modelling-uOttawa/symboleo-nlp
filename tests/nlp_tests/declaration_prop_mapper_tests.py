import unittest
from unittest.mock import MagicMock

from app.classes.elements.all_elements import *
from app.classes.spec.declaration import DeclarationProp
from app.src.sym_updaters.custom_event.declaration_prop_mapper import DeclarationPropMapper

from app.classes.other.helpers import ClassHelpers
from tests.helpers.test_objects import CustomEvents

subj_test_suite = [
    (
        CustomEvents.occupy_property(),
        DeclarationProp('occupying_agent', 'renter', 'Role')
    )
]

dobj_test_suite = [
    (
        CustomEvents.occupy_property(),
        DeclarationProp('occupied_object', 'property', 'RentalProperty')
    )
]

pp_test_suite = [
    (
        CustomEvents.eating_pie(),
        [
            DeclarationProp('eating_co_agent', 'the seller', 'Role')
        ]
    )
]

class DeclarationPropMapperFullTests(unittest.TestCase):
    def setUp(self) -> None:
        # Wil prob need to add deps...
        self.sut = DeclarationPropMapper()


    def test_mapping_subject(self):
        for evt, exp_val in subj_test_suite:
            res = self.sut.map_subject(evt.subj, evt)
            self.assertEqual(res, exp_val)
    

    def test_mapping_dobject(self):
        for evt, exp_val in dobj_test_suite:
            res = self.sut.map_dobject(evt.dobj, evt)
            self.assertEqual(res, exp_val)
    

    def test_mapping_pp(self):
        for evt, exp_val in pp_test_suite:
            res = [self.sut.map_prep_phrase(pp, evt) for pp in evt.pps]
            
            # for x in res:
            #     x.print_me()
            
            lists_eq = ClassHelpers.lists_eq(res, exp_val, 'key')
            self.assertTrue(lists_eq)


if __name__ == '__main__':
    unittest.main()