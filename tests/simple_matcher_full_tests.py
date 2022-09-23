import unittest
from app.lib.matchers.matchers_builder import MatchersBuilder
from tests.helpers.test_nlp import TestNLP

test_suite = [
    {
        'sentence': 'the sky is blue',
        'sym': 'occurs(is_blue(sky), X)'
    },
    {
        'sentence': 'the cat is angry',
        'sym': 'occurs(is_angry(cat), X)'
    }
]

class SimpleMatcherFullTests(unittest.TestCase):
    def setUp(self):
        self.__nlp = TestNLP.get_nlp()
        self.sut = MatchersBuilder.build_simple_matcher(self.__nlp)

    def test_simple_matcher(self):
        for x in test_suite:
            doc = self.__nlp(x['sentence'])

            result = self.sut.try_match(doc)
            self.assertEqual(result.to_sym(), x['sym'])

if __name__ == '__main__':
    unittest.main()