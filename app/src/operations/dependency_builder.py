from app.classes.operations.dependencies import Dependencies
from tests.helpers.test_nlp import TestNLP

class DependencyBuilder:
    def build(fake:bool = False):
        # TODO: Would be better to just have a FakeNLP... but may be too much work
        if not fake:
            nlp = TestNLP.get_nlp()
        else:
            nlp = None

        # Might add the contract here...
        return Dependencies(
            nlp = nlp,
            fake = fake
        )