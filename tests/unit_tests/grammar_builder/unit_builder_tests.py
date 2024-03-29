import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import BeforeUnit
from app.classes.helpers.list_eq import ClassHelpers
from app.src.grammar_builder.unit_builders.dobj_ub import DobjUB
from app.src.grammar_builder.unit_builders.contract_action_ub import ContractActionUB
from app.src.grammar_builder.unit_builders.subject_ub import SubjectUB
from app.src.grammar_builder.unit_builders.time_unit_ub import TimeUnitUB
from app.src.grammar_builder.unit_builders.unit_builder import DefaultUnitBuilder
from app.src.grammar_builder.unit_builders.linking_verb_ub import LinkingVerbUB
from app.src.grammar_builder.unit_builders.time_period_ub import TimePeriodUB
from app.src.grammar_builder.unit_builders.notifier_unit_ub import NotifierUnitUB

from tests.helpers.test_contract import get_test_contract


class UnitBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = DobjUB()


    def test_linking_ub(self):
        ub = LinkingVerbUB()
        contract = get_test_contract()
        result = ub.build('', contract)
        self.assertTrue(ClassHelpers.simple_lists_eq(result.options, ['become', 'becomes']))


    def test_time_period_ub(self):
        ub = TimePeriodUB()
        contract = get_test_contract()
        result = ub.build('', contract)
        self.assertTrue(ClassHelpers.simple_lists_eq(result.options, ['the contract period']))

    def test_dobj_ub(self):
        ub = DobjUB()
        contract = get_test_contract()
        result = ub.build('', contract)
        self.assertTrue(ClassHelpers.simple_lists_eq(result.options, ['test_role', 'test_asset']))

    def test_contract_action_ub(self):
        ub = ContractActionUB()
        contract = get_test_contract()
        result = ub.build('', contract)
        self.assertIn('terminated', result.options)

    def test_notifier_unit_ub(self):
        ub = NotifierUnitUB()
        contract = get_test_contract()
        result = ub.build('', contract)
        self.assertIn('test_role', result.options)


    def test_subj_ub(self):
        ub = SubjectUB()
        contract = get_test_contract()
        result = ub.build('', contract)
        self.assertTrue(ClassHelpers.simple_lists_eq(result.options, ['test_role', 'test_asset']))

    def test_time_unit_ub(self):
        ub = TimeUnitUB()
        contract = get_test_contract()
        result = ub.build('', contract)
        self.assertIn('weeks', result.options)

    def test_default_ub(self):
        ub = DefaultUnitBuilder()
        contract = get_test_contract()
        result = ub.build('BEFORE', contract)
        self.assertEqual(type(result), BeforeUnit)

if __name__ == '__main__':
    unittest.main()
