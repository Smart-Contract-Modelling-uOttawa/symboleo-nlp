import unittest
from unittest.mock import MagicMock

from app.classes.grammar.node_type import NodeType
from app.src.helpers.template_getter import get_template
from app.src.grammar.grammar_generator import GrammarGenerator
from app.src.grammar.grammar_config import GrammarGeneratorConfig
from app.src.grammar.helpers.domain_timepoint_extractor import IExtractDomainTimePoints


# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class GrammarGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.domain_timepoint_extractor = IExtractDomainTimePoints()
        self.domain_timepoint_extractor.extract = MagicMock(return_value = ['evt.due_date'])
        self.gg = GrammarGenerator(self.domain_timepoint_extractor)

    def test_grammar_generator(self):
        contract_template = get_template('sample_raw')
        config = GrammarGeneratorConfig()

        root_node = self.gg.generate(contract_template, config)

        self.assertEqual(self.domain_timepoint_extractor.extract.call_count, 1)
        self.assertEqual(root_node.id, 'Root')
        self.assertEqual(root_node.node_type, NodeType.ROOT)


if __name__ == '__main__':
    unittest.main()