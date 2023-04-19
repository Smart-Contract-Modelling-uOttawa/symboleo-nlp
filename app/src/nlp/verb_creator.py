from enum import Enum

class VerbType(Enum):
    TRANSITIVE = 0,
    LINKING = 1,
    INTRANSITIVE = 2,
    #...


class Verb:
    def __init__(self, verb_str: str, verb_type: VerbType):
        self.verb_str = verb_str
        self.verb_type = verb_type


class ICreateVerbs:
    def create(self, verb_str: str):
        raise NotImplementedError()


class VerbCreator(ICreateVerbs):
    def __init__(self):
        self.s = 0
        # validator, conjugator, type_getter...

    def create(self, verb_str: str):
        self._validate(verb_str)

        conj_verb = self._conjugate(verb_str)
        verb_type = self._get_verb_type(conj_verb)

        # Get type (transitive, intransitive, linking, ...)
        return Verb(conj_verb, verb_type)
    
    def _validate(self, verb_str):
        #...
        valid = True

        if valid:
            return verb_str
        
        raise ValueError('Invalid verb...')
    

    def _conjugate(self, verb_str: str):
        # ...
        return verb_str
    

    def _get_verb_type(self, verb_str) -> VerbType:
        # ...
        return VerbType.TRANSITIVE