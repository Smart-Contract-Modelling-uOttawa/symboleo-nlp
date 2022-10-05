from app.classes.spec.primitive import Primitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

class IExtractPrimitives:
    def extract(self, doc) -> list[Primitive]:
        raise NotImplementedError()

class PrimitiveExtractor(IExtractPrimitives):
    def __init__(
        self,
        primitive_identifiers: list[IIdentifyPrimitives],
        threshold: float
    ):
        self.__threshold = threshold
        self.__identifiers = primitive_identifiers
    

    def extract(self, doc) -> list[Primitive]:
        results = [x.identify(doc) for x in self.__identifiers]
        return [x for x in results if x.score > self.__threshold]

