import unittest
from unittest.mock import MagicMock
from app.src.nlp.statement_extractor import StatementExtractor,Statement

from tests.helpers.test_nlp import TestNLP

# Might also make a separate test set for NLP functionality - keep it out of regular unit test folder

test_cases = [
    ('the sky is blue', Statement('the sky', 'is', 'blue')), # Do I want to keep "the" in?
    ('legal proceedings become necessary', Statement('legal proceedings', 'become', 'necessary')),
    ('the seller is satisfied', Statement('the seller', 'is', 'satisfied')),
    ('all blorgs are blargs', Statement('all blorgs', 'are', 'blargs')),
    ('the world is a vampire', Statement('the world', 'is', 'a vampire'))
    # Add more tests....
]

# Expected failures
negative_test_cases = [
    # Add expected failures

]

class StatementExtractorTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        self.sut = StatementExtractor(nlp)
    
    def test_statement_extractor(self):
        for s, expected in test_cases:
            result = self.sut.extract(s)
            self.assertEqual(result, expected)
    
if __name__ == '__main__':
    unittest.main()