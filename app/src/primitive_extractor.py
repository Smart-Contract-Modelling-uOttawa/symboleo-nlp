from app.classes.spec.primitive import Primitive


class IExtractPrimitives:
    def extract(self, doc) -> list[Primitive]:
        raise NotImplementedError()


class PrimitiveExtractor(IExtractPrimitives):
    def __init__(self):
        self.s = 0
    
    # TODO: ...
    def extract(self, doc) -> list[Primitive]:
        # Find the most likely candidates, and create them
        # May use a scoring system as well
        # May reuse the dynamic constructor... Or use separate ones
        return []
