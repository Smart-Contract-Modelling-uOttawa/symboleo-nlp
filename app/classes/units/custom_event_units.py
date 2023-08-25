from app.classes.units.unit_variety import UnitVariety
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class PrepUnit(InputUnit):
    unit_type = UnitType.PREP_PHRASE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Prep Phrase'
    info = 'Enter a prepositional phrase (preposition followed by a noun phrase)'

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

class TransitiveVerbUnit(InputUnit):
    unit_type = UnitType.TRANSITIVE_VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Transitive Verb'

class IntransitiveVerbUnit(InputUnit):
    unit_type = UnitType.INTRANSITIVE_VERB
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Intransitive Verb'

class LinkingVerbUnit(InputUnit):
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

