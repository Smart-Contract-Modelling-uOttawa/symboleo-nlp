from app.classes.operations.dependencies import Dependencies
from tests.helpers.test_nlp import TestNLP

class DependencyBuilder:
    def build():
        nlp = TestNLP.get_nlp()

        # Might add the contract here...
        return Dependencies(
            nlp = nlp
        )