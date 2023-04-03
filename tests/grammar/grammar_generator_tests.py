import unittest
from unittest.mock import MagicMock

from app.classes.grammar.node_type import NodeType
from app.src.helpers.template_getter import get_template
from app.src.grammar.grammar_generator import GrammarGenerator
from app.src.grammar.grammar_config import GrammarGeneratorConfig
from app.src.grammar.helpers.domain_timepoint_extractor import IExtractDomainTimePoints
from app.src.operations.parm_configs import ParmOpCode

# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class GrammarGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.domain_timepoint_extractor = IExtractDomainTimePoints()
        self.domain_timepoint_extractor.extract = MagicMock(return_value = ['evt.due_date'])
        self.gg = GrammarGenerator(self.domain_timepoint_extractor)

    def test_grammar_generator_op1(self):
        contract_template = get_template('sample_raw')
        config = GrammarGeneratorConfig(op_codes = [ParmOpCode.REFINE_PREDICATE])

        root_node = self.gg.generate(contract_template, config)

        self.assertEqual(self.domain_timepoint_extractor.extract.call_count, 1)
        self.assertEqual(root_node.id, 'Root')
        self.assertEqual(root_node.node_type, NodeType.ROOT)


    def test_grammar_generator_op2(self):
        contract_template = get_template('sample_raw')
        config = GrammarGeneratorConfig(op_codes = [ParmOpCode.ADD_TRIGGER])

        root_node = self.gg.generate(contract_template, config)

        self.assertEqual(self.domain_timepoint_extractor.extract.call_count, 1)
        self.assertEqual(root_node.id, 'Root')
        self.assertEqual(root_node.node_type, NodeType.ROOT)


    def test_grammar_generator_no_op(self):
        contract_template = get_template('sample_raw')
        config = GrammarGeneratorConfig()

        root_node = self.gg.generate(contract_template, config)

        self.assertEqual(self.domain_timepoint_extractor.extract.call_count, 1)
        self.assertEqual(root_node.id, 'Root')
        self.assertEqual(root_node.node_type, NodeType.ROOT)


if __name__ == '__main__':
    unittest.main()