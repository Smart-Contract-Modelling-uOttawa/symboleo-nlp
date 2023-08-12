import unittest
from unittest.mock import MagicMock

from typing import Dict
from app.classes.spec.domain_model import DomainModel, Role, Asset
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration
from tests.helpers.test_objects import NounPhrases
from tests.helpers.test_nlp import TestNLP
from tests.helpers.test_obj_lib.isolated_test_objects import Verbs as IVP
from tests.helpers.test_contract import get_test_contract_for_assets
from app.src.custom_event_extractor.verb.verb_extractor import VerbExtractor
from app.src.custom_event_extractor.nlp.lemmatizer import Lemmatizer
from app.src.custom_event_extractor.verb.conjugator import MyConjugator
from app.src.custom_event_extractor.verb.conjugator import ML3Conjugator
from app.src.custom_event_extractor.noun_phrase.asset_type_extractor import AssetTypeExtractor

test_suite = [
    # isolated tests
    ('submits', IVP.submit()),
    ('returns', IVP.return_verb()),
]

# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class NounPhraseExtractorTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        lemmatizer = Lemmatizer(nlp)
        inner_conjugator = ML3Conjugator(language='en')
        conjugator = MyConjugator(inner_conjugator)
        self.sut = VerbExtractor(lemmatizer, conjugator)

    @unittest.skip('may fix...')
    def test_np_extractor(self):
        contract = get_test_contract_for_assets()

        for test_val, exp_val in test_suite:
            res = self.sut.extract(test_val, contract)
            # res.print_me()
            # print('----')
            # exp_val.print_me()
            self.assertEqual(res, exp_val)

if __name__ == '__main__':
    unittest.main()