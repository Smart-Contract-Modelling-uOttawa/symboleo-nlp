from app.classes.spec.primitive import ScoredPrimitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

class IExtractPrimitives:
    def extract(self, doc) -> list[ScoredPrimitive]:
        raise NotImplementedError()

# TODO: May alter this one - e.g. by including the scores
## May include a decider to limit to certain configs, e.g. dont want both  a powerEvent and ObligationEvent?
## May end up having quite a bit of orchestration involved
class PrimitiveExtractor(IExtractPrimitives):
    def __init__(
        self,
        primitive_identifiers: list[IIdentifyPrimitives]
    ):
        self.__identifiers = primitive_identifiers
        self.__threshold = 0
    

    def extract(self, doc) -> list[ScoredPrimitive]:
        results = [x.identify(doc) for x in self.__identifiers]
        return [x for x in results if x.score > self.__threshold]

