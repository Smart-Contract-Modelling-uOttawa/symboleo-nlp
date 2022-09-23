from app.classes.spec.symboleo_spec import NegAtom

class IMatcher:
    def try_match(self, doc) -> NegAtom:
        raise NotImplementedError()


class IValidateMatches:
    def validate(self, doc) -> bool:
        raise NotImplementedError()