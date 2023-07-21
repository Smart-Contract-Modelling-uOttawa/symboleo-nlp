from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class PrepUnit(InputUnit):
    unit_type = UnitType.PREP_PHRASE
    prompt = 'Preposition'
    needs_value = True

class AdverbUnit(InputUnit):
    unit_type = UnitType.ADVERB
    prompt = 'Adverb'
    needs_value = True

class PredicateUnit(InputUnit):
    unit_type = UnitType.PREDICATE
    prompt = 'Predicate'
    needs_value = True

class DobjUnit(InputUnit):
    unit_type = UnitType.DOBJ
    prompt = 'Direct Object'
    needs_value = True

class VerbUnit(InputUnit):
    unit_type = UnitType.VERB
    prompt = 'Verb'
    needs_value = True

class TransitiveVerbUnit(VerbUnit):
    unit_type = UnitType.TRANSITIVE_VERB
    prompt = 'Transitive Verb'
    needs_value = True

class IntransitiveVerbUnit(VerbUnit):
    unit_type = UnitType.INTRANSITIVE_VERB
    prompt = 'Intransitive Verb'
    needs_value = True

class LinkingVerbUnit(VerbUnit):
    unit_type = UnitType.LINKING_VERB
    prompt = 'Linking Verb'
    needs_value = True

class SubjectUnit(InputUnit):
    unit_type = UnitType.SUBJECT
    prompt = 'Subject'
    needs_value = True

class CustomEventUnit(InputUnit):
    unit_type = UnitType.CUSTOM_EVENT
    prompt = 'Custom event'

