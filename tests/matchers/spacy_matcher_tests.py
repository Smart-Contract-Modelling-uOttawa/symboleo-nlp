import unittest
from spacy.matcher import Matcher

from tests.helpers.test_nlp import TestNLP

matcher_test_suite = [
    {
        'pattern': [{"TAG": "DT"}, {"TAG": "NN"}, {"TAG": "VBZ"}, {"TAG": "JJ"}],
        'positive': [
            'the sky is blue',
            'the cat is angry'
        ],
        'negative': [
            'call me Ishmael',
            'it is raining'
        ]
    },

    {
        'pattern': [{"TAG": "PRP"}, {"TAG": "VBZ"}, {"TAG": "VBG"}],
        'positive': [
            'it is raining'
        ],
        'negative': [
            'call me Ishmael',
            'the sky is blue'
        ]
    },

    ##...
]


class SpacyMatcherTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.key = 'test_key'

    def test_spacy_matcher(self):
        for x in matcher_test_suite:
            matcher = Matcher(self.nlp.vocab)
            matcher.add(self.key, [x['pattern']])

            ## Run the positive tests
            for p in x['positive']:
                doc = self.nlp(p)
                matches = matcher(doc)

                self.assertEqual(len(matches), 1)
                res1 = matches[0]
                key_ind, _, _ = res1
                res1_key = self.nlp.vocab.strings[key_ind]
                self.assertEqual(res1_key, self.key)
            
            ## Run the negative tests
            for n in x['negative']:
                doc = self.nlp(n)
                matches = matcher(doc)
                self.assertEqual(len(matches), 0)

        
if __name__ == '__main__':
    unittest.main()