import unittest
from unittest.mock import MagicMock
import copy

from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName, ObligationEvent, ObligationEventName
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.selection.all_nodes import *
from app.classes.custom_event.conj_type import ConjType
from app.classes.operations.user_input import UserInput
from app.classes.other.helpers import ClassHelpers

from app.src.operations.dependency_builder import DependencyBuilder
from app.src.sym_updaters.sym_updater_dict import SymUpdaterDictConstructor
from app.src.sym_updaters.update_extractor import UpdateExtractor

from app.src.frame_updaters.frame_builder_builder import FrameBuilderBuilder

from app.src.grammar.input_converter_builder import InputConverterBuilder

from tests.helpers.sample_norm_lib import SampleNorms


#from app.templates.template_getter import get_template

# This will grow into a full-tester
class ObligationEventTests(unittest.TestCase):
    def setUp(self):
        deps = DependencyBuilder.build(fake=True)

        self.input_converter = InputConverterBuilder.build(deps)

        updater_dict = SymUpdaterDictConstructor.build(deps)
        self.sym_updater = UpdateExtractor(updater_dict)

        self.frame_builder = FrameBuilderBuilder.build()

    def test_contract_event(self):
        #contract = get_template('sample_t')
        ob_key = 'ob_test'
        
        user_input = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.NORM_EVENT),
            UserInput(NodeType.OBLIGATION_SUBJECT, ob_key),
            UserInput(NodeType.OBLIGATION_ACTION, 'Violated')
        ]

        node_list = self.input_converter.convert(user_input)

        exp_node_list = [
            RootNode(),
            IfNode(),
            EventNode(),
            StandardEventNode(),
            NormEventNode(),
            ObligationSubjectNode(ObligationSubject(ob_key)),
            ObligationActionNode(ObligationEventName.Violated)
        ]

        # Is this acceptable??? OR should it be more explicit
        exp_nl = 'if ob_test obligation is violated'

        norm = SampleNorms.get_sample_norm()
        expected_norm = copy.deepcopy(norm)
        expected_norm.update(
            'trigger', 
            PredicateFunctionHappens(
                ObligationEvent(ObligationEventName.Violated, ob_key)
            )
        )

        frame_result = self.frame_builder.build(node_list)  
        sym_result = self.sym_updater.extract(norm, node_list)
        norm_results = sym_result.norms
        
        # Expected result
        self.assertEqual(exp_nl, frame_result.to_text())
        self.assertEqual(len(norm_results), 1)
        self.assertEqual(norm_results[0].to_sym(), expected_norm.to_sym())




        


if __name__ == '__main__':
    unittest.main()