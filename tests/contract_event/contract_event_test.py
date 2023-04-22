import unittest
from unittest.mock import MagicMock
import copy

from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent
from app.classes.selection.all_nodes import *
from app.classes.custom_event.conj_type import ConjType
from app.classes.operations.user_input import UserInput
from app.classes.other.helpers import ClassHelpers

from app.src.operations.dependency_builder import DependencyBuilder
from app.src.sym_updaters.updater_dict import UpdaterDictConstructor
from app.src.sym_updaters.update_extractor import UpdateExtractor

from app.src.frames.frame_builder_builder import FrameBuilderBuilder

from app.src.operations.input_converter_builder import InputConverterBuilder

from tests.helpers.sample_norm_lib import SampleNorms


#from app.templates.template_getter import get_template

# This will grow into a full-tester
class ContractEventTests(unittest.TestCase):
    def setUp(self):
        deps = DependencyBuilder.build()

        self.input_converter = InputConverterBuilder.build(deps)

        updater_dict = UpdaterDictConstructor.build(deps)
        self.sym_updater = UpdateExtractor(updater_dict)

        self.frame_builder = FrameBuilderBuilder.build()

    def test_contract_event(self):
        #contract = get_template('sample_t')
        
        user_input = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.BEFORE),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated')
        ]

        node_list_result = self.input_converter.convert(user_input)

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

        frame_result = self.frame_builder.build(node_list_result)  
        sym_result = self.sym_updater.extract(norm, node_list_result)
        norm_results = sym_result.norms
        
        # Expected result
        self.assertEqual(exp_nl, frame_result.to_text())
        self.assertEqual(len(norm_results), 1)
        self.assertEqual(norm_results[0].to_sym(), expected_norm.to_sym())




        


if __name__ == '__main__':
    unittest.main()
