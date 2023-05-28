from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.custom_event.verb import Verb
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.prep_phrase import PrepPhrase
from app.classes.custom_event.adverb import Adverb
from app.classes.custom_event.predicate import Predicate

class PrepElement(Element[PrepPhrase]):
    unit_type = UnitType.PREP_PHRASE

class AdverbElement(Element[Adverb]):
    unit_type = UnitType.ADVERB
    
class PredicateElement(Element[Predicate]):
    unit_type = UnitType.PREDICATE
    
class DobjElement(Element[NounPhrase]):
    unit_type = UnitType.DOBJ

class VerbElement(Element[Verb]):
    unit_type = UnitType.VERB

class FailsToElement(Element):
    unit_type = UnitType.FAILS_TO

class SubjectElement(Element[NounPhrase]):
    unit_type = UnitType.SUBJECT

class CustomEventElement(Element[CustomEvent]):
    unit_type = UnitType.CUSTOM_EVENT