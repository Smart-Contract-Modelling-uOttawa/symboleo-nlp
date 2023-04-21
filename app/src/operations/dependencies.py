from tests.helpers.test_nlp import TestNLP
from app.classes.spec.symboleo_contract import ISymboleoContract

class Dependencies:
    def __init__(self, nlp):
        self.nlp = nlp

class DependencyBuilder:
    def build():
        nlp = TestNLP.get_nlp()

        # Might add the contract here...
        return Dependencies(
            nlp = nlp
        )
