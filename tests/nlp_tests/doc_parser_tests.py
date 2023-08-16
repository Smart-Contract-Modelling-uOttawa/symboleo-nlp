import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from app.src.nlp.fake_doc_parser import FakeDocParser
from app.src.nlp.doc_parser import DocParser

# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class DocParserTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        self.sut = DocParser(nlp)

    def test_doc_parser(self):
        test_dp = FakeDocParser()
        test_dict = test_dp.get_dict()

        for x in test_dict:
            exp_val = test_dict[x]
            result = self.sut.parse(x)

            # print(x)
            # result.print_me()
            # exp_val.print_me()

            self.assertEqual(result, exp_val)

if __name__ == '__main__':
    unittest.main()