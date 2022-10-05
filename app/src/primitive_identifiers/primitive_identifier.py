from app.classes.spec.primitive import ScoredPrimitive

class IIdentifyPrimitives:
    def identify(self, doc) -> ScoredPrimitive:
        raise NotImplementedError()