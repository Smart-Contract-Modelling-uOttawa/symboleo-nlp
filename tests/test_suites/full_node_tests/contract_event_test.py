import unittest
from unittest.mock import MagicMock
import copy

from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent
from app.classes.elements.all_elements import *
from app.classes.events.conj_type import ConjType
from app.classes.operations.user_input import UserInput
from app.classes.other.helpers import ClassHelpers

from app.src.operations.dependency_builder import DependencyBuilder
from app.src.sym_updaters.sym_updater_dict import SymUpdaterDictConstructor
from app.src.sym_updaters.update_extractor import UpdateExtractor

from app.src.pattern_builder.pattern_builder_builder import PatternBuilderBuilder

from app.src.selection.element_extractor_builder import ElementExtractorBuilder

from tests.helpers.sample_norm_lib import SampleNorms


#from app.templates.template_getter import get_template

# This will grow into a full-tester
# Make a test suite: UserInput nodes, expected NL, expected UpdateObject
class ContractEventTests(unittest.TestCase):
    def setUp(self):
        deps = DependencyBuilder.build(fake=True)

        self.element_extractor = ElementExtractorBuilder.build(deps)

        updater_dict = SymUpdaterDictConstructor.build(deps)
        self.sym_updater = UpdateExtractor(updater_dict)

        self.pattern_builder = PatternBuilderBuilder.build()

    def test_contract_event(self):
        #contract = get_template('sample_t')
        
        user_input = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.BEFORE),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'terminates')
        ]

        node_list_result = self.element_extractor.extract(user_input)

        exp_node_list = [
            RootNode(),
            BeforeNode(),
            EventNode(),
            StandardEventNode(),
            ContractEventNode(),
            ContractSubjectNode(),
            ContractActionNode(ContractEventName.Terminated)
        ]

        exp_nl = 'before contract terminates'
        norm = SampleNorms.get_sample_norm()
        expected_norm = copy.deepcopy(norm)
        expected_norm.update(
            'consequent', 
            PredicateFunctionWHappensBeforeEvent(
                VariableEvent('action'),
                ContractEvent(ContractEventName.Terminated) 
            )
        )

        pattern_result = self.pattern_builder.build(node_list_result)  
        sym_result = self.sym_updater.extract(norm, node_list_result)
        norm_results = sym_result.norms
        
        # Expected result
        self.assertEqual(exp_nl, pattern_result.to_text())
        self.assertEqual(len(norm_results), 1)
        self.assertEqual(norm_results[0].to_sym(), expected_norm.to_sym())




        


if __name__ == '__main__':
    unittest.main()
