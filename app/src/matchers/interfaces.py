from app.classes.spec.symboleo_spec import PNegAtom

class IMatcher:
    def try_match(self, doc) -> PNegAtom:
        raise NotImplementedError()

class IValidateMatches:
    def validate(self, doc) -> bool:
        raise NotImplementedError()