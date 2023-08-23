from app.classes.operations.dependencies import Dependencies
from app.src.nlp.nlp_getter import NLPGetter

class DependencyBuilder:
    def build(fake:bool = False):
        if not fake:
            nlp = NLPGetter.get()
        else:
            nlp = None

        return Dependencies(
            nlp = nlp,
            fake = fake
        )