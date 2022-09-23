import unittest
from app.lib.matchers.matchers_builder import MatchersBuilder
from app.lib.norm_updater import NormUpdater
from tests.helpers.test_nlp import TestNLP

from app.lib.sentence_obligation_converter import SentenceObligationConverter
from app.classes.spec.symboleo_spec import Norm

from app.templates.meat_sale.norms import meat_sale_norms
from tests.helpers.meat_sale_test_suite import meat_sale_test_suite as test_suite

# Main full-stack test suite
class MainTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.norms = meat_sale_norms

        matcher_builder = MatchersBuilder(self.nlp)
        matchers = matcher_builder.build()
        norm_updater = NormUpdater()

        self.sut = SentenceObligationConverter(self.nlp, matchers, norm_updater)

    def test_simple_matcher(self):
        for x in test_suite:
            norm_set: list[Norm] = self.norms[x.norm_type]
            norm = [n for n in norm_set if n.id == x.id][0]
            result = self.sut.convert(x.customization, norm, x.str_component)

            self.assertEqual(result.to_sym(), x.expected_sym)


if __name__ == '__main__':
    unittest.main()