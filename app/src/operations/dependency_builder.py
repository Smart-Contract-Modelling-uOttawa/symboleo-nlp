from app.classes.operations.dependencies import Dependencies
from tests.helpers.test_nlp import TestNLP

class DependencyBuilder:
    def build(fake:bool = False, use_new = True):
        if not fake:
            nlp = TestNLP.get_nlp()
        else:
            nlp = None

        return Dependencies(
            nlp = nlp,
            fake = fake,
            use_new=use_new
        )