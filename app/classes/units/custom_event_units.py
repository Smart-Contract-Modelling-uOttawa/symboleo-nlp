from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class PrepUnit(InputUnit):
    unit_type = UnitType.PREP_PHRASE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Preposition'
    needs_value = True

class AdverbUnit(InputUnit):
    unit_type = UnitType.ADVERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Adverb'
    needs_value = True

class PredicateUnit(InputUnit):
    unit_type = UnitType.PREDICATE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Predicate'
    needs_value = True

class DobjUnit(InputUnit):
    unit_type = UnitType.DOBJ
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Direct Object'
    needs_value = True

class VerbUnit(InputUnit):
    unit_type = UnitType.VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Verb'
    needs_value = True

class TransitiveVerbUnit(VerbUnit):
    unit_type = UnitType.TRANSITIVE_VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Transitive Verb'
    needs_value = True

class IntransitiveVerbUnit(VerbUnit):
    unit_type = UnitType.INTRANSITIVE_VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Intransitive Verb'
    needs_value = True

class LinkingVerbUnit(VerbUnit):
    unit_type = UnitType.LINKING_VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Linking Verb'
    needs_value = True

class SubjectUnit(InputUnit):
    unit_type = UnitType.SUBJECT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Subject'
    needs_value = True

class CustomEventUnit(InputUnit):
    unit_type = UnitType.CUSTOM_EVENT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Custom event'

