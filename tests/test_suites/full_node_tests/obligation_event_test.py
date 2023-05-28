import unittest
from unittest.mock import MagicMock
import copy

from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName, ObligationEvent, ObligationEventName
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.elements.all_nodes import *
from app.classes.custom_event.conj_type import ConjType
from app.classes.operations.user_input import UserInput
from app.classes.other.helpers import ClassHelpers

from app.src.operations.dependency_builder import DependencyBuilder
from app.src.sym_updaters.sym_updater_dict import SymUpdaterDictConstructor
from app.src.sym_updaters.update_extractor import UpdateExtractor

from app.src.pattern_updaters.pattern_builder_builder import PatternBuilderBuilder

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

        self.pattern_builder = PatternBuilderBuilder.build()


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
            UserInput(NodeType.OBLIGATION_ACTION, 'Violated'),
            UserInput(NodeType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(NodeType.SUBJECT, 'buyer'),
            UserInput(NodeType.FAILS_TO),
            UserInput(NodeType.VERB, 'pay'),
            UserInput(NodeType.DOBJ, '$100'),
            UserInput(NodeType.PREP_PHRASE, 'in CAD'),
            UserInput(NodeType.PREP_PHRASE, 'to seller'),
            UserInput(NodeType.PREP_PHRASE, 'by March 30, 2024'),
            UserInput(NodeType.FINAL_NODE)
        ]

        node_list = self.input_converter.convert(user_input)

        for x in node_list:
            print(x)

        # exp_node_list = [
        #     RootNode(),
        #     IfNode(),
        #     EventNode(),
        #     StandardEventNode(),
        #     NormEventNode(),
        #     ObligationSubjectNode(ObligationSubject(ob_key)),
        #     ObligationActionNode(ObligationEventName.Violated)
        # ]

        exp_nl = 'if buyer fails to pay $100 in CAD to seller by March 30, 2024'

        norm = SampleNorms.get_sample_norm()
        expected_norm = copy.deepcopy(norm)
        expected_norm.update(
            'trigger', 
            PredicateFunctionHappens(
                ObligationEvent(ObligationEventName.Violated, ob_key)
            )
        )

        pattern_result = self.pattern_builder.build(node_list)  
        
        sym_result = self.sym_updater.extract(norm, node_list)
        norm_results = sym_result.norms
        print(norm_results[0].to_sym())
        
        # Expected result
        self.assertEqual(exp_nl, pattern_result.to_text())
        self.assertEqual(len(norm_results), 1)
        self.assertEqual(norm_results[0].to_sym(), expected_norm.to_sym())




        


if __name__ == '__main__':
    unittest.main()
