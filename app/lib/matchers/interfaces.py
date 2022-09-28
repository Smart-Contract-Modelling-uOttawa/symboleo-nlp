from app.classes.spec.symboleo_spec import PAtom

class IMatcher:
    def try_match(self, doc) -> PAtom:
        raise NotImplementedError()

class IValidateMatches:
    def validate(self, doc) -> bool:
        raise NotImplementedError()