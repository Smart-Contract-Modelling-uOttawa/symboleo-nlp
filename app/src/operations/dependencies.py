from tests.helpers.test_nlp import TestNLP

class Dependencies:
    def __init__(self, nlp):
        self.nlp = nlp

class DependencyBuilder:
    def build():
        nlp = TestNLP.get_nlp()

        return Dependencies(
            nlp = nlp
        )
