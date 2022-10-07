import unittest
from unittest.mock import MagicMock

from app.src.primitive_extractor import PrimitiveExtractor
from app.src.primitive_identifiers.obligation_event_identifier import ObligationEventIdentifier
from app.src.primitive_identifiers.power_event_identifier import PowerEventIdentifier
from app.src.primitive_identifiers.contract_event_identifier import ContractEventIdentifier
from app.src.primitive_identifiers.event_scorer import EventScorer
from app.src.primitive_identifiers.variable_scorer import VariableScorer
from app.src.primitive_identifiers.similarity_calculator import SentenceSimilarityCalculator
from app.src.primitive_identifiers.sentence_preprocessor import SentencePreprocessor
from app.templates.meat_sale.templates import meat_sale_templates
from app.src.primitive_identifiers.dicts.event_dict_set_builder import EventDictSetBuilder

from tests.test_suites.full_test_suite import full_test_suite
from tests.helpers.test_nlp import TestNLP

class FullPrimitiveExtractorTests(unittest.TestCase):
    def setUp(self):
        event_dicts = EventDictSetBuilder.build_all()
        self.nlp = TestNLP.get_nlp()

        preprocessor = SentencePreprocessor(self.nlp)
        similarity_calculator = SentenceSimilarityCalculator(preprocessor)

        # ObligationEvent
        self.ob_event_scorer = EventScorer(event_dicts['obligation'])
        obligation_sent_dict = meat_sale_templates['obligations']
        self.ob_var_scorer = VariableScorer(self.nlp, obligation_sent_dict, similarity_calculator)
        self.oe_identifier = ObligationEventIdentifier(self.ob_event_scorer, self.ob_var_scorer)

        # PowerEvent
        power_event_scorer = EventScorer(event_dicts['power'])
        power_sent_dict = meat_sale_templates['powers']
        power_var_scorer = VariableScorer(self.nlp, power_sent_dict, similarity_calculator)
        self.pe_identifier = PowerEventIdentifier(power_event_scorer, power_var_scorer)

        # ContractEvent
        c_event_scorer = EventScorer(event_dicts['contract'])
        self.ce_identifier = ContractEventIdentifier(c_event_scorer)

        self.primitive_extractor = PrimitiveExtractor([
            self.oe_identifier,
            self.pe_identifier,
            self.ce_identifier
        ])

    @unittest.skip
    def test_event_scorer(self):
        x = full_test_suite[1]
        sent = x['sentence']
        doc = self.nlp(sent)
        event_score = self.ob_event_scorer.score(doc)
        print(event_score)

        var_score = self.ob_var_scorer.score(doc)
        print(var_score)

    @unittest.skip
    def test_oe(self):
        x = full_test_suite[1]
        sent = x['sentence']
        doc = self.nlp(sent)
        result = self.oe_identifier.identify(doc)
        print(type(result.primitive))
        print(result.score)


    @unittest.skip
    def test_full_primitive_extractor(self):
        for x in full_test_suite:
            sent = x['sentence']
            print(f'\n========= {sent} ==============')
            exp_primitives = x['primitives']

            doc = self.nlp(sent)
            results = self.primitive_extractor.extract(doc)
            results.sort(key=lambda x: x.score, reverse=True)

            for r in results:
                print(f'- {type(r.primitive).__name__}: {r.primitive.to_sym()} ({r.score})')

            for i,xp in enumerate(exp_primitives):
                self.assertTrue(results[i].primitive == xp)


            


  
if __name__ == '__main__':
    unittest.main()