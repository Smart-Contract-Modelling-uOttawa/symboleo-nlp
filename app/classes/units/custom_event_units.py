from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType
from app.classes.units.final_unit import FinalUnit

class PrepUnit(InputUnit):
    unit_type = UnitType.PREP_PHRASE
    prompt = 'Preposition'
    needs_value = True
    children = [FinalUnit]

class AdverbUnit(InputUnit):
    unit_type = UnitType.ADVERB
    prompt = 'Adverb'
    children = [PrepUnit, FinalUnit]
    needs_value = True

class PredicateUnit(InputUnit):
    unit_type = UnitType.PREDICATE
    prompt = 'Predicate'
    children = [AdverbUnit, FinalUnit]
    needs_value = True

class DobjUnit(InputUnit):
    unit_type = UnitType.DOBJ
    prompt = 'Direct Object'
    children = [AdverbUnit, FinalUnit]
    needs_value = True

class VerbUnit(InputUnit):
    unit_type = UnitType.VERB
    prompt = 'Verb'
    children = [DobjUnit, AdverbUnit, PredicateUnit, FinalUnit]
    needs_value = True

class SubjectUnit(InputUnit):
    unit_type = UnitType.SUBJECT
    prompt = 'Subject'
    children = [VerbUnit]
    needs_value = True

class CustomEventUnit(InputUnit):
    unit_type = UnitType.CUSTOM_EVENT
    prompt = 'Custom event'
    children = [SubjectUnit]

