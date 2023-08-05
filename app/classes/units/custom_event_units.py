from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class PrepUnit(InputUnit):
    unit_type = UnitType.PREP_PHRASE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Preposition'

class AdverbUnit(InputUnit):
    unit_type = UnitType.ADVERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Adverb'

class PredicateUnit(InputUnit):
    unit_type = UnitType.PREDICATE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Predicate'

class DobjUnit(InputUnit):
    unit_type = UnitType.DOBJ
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Direct Object'

class VerbUnit(InputUnit):
    unit_type = UnitType.VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Verb'

class TransitiveVerbUnit(VerbUnit):
    unit_type = UnitType.TRANSITIVE_VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Transitive Verb'

class IntransitiveVerbUnit(VerbUnit):
    unit_type = UnitType.INTRANSITIVE_VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Intransitive Verb'

class LinkingVerbUnit(VerbUnit):
    unit_type = UnitType.LINKING_VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Linking Verb'

class SubjectUnit(InputUnit):
    unit_type = UnitType.SUBJECT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Subject'

class CustomEventUnit(InputUnit):
    unit_type = UnitType.CUSTOM_EVENT
    unit_var = UnitVariety.EMPTY
    prompt = 'Custom event'

