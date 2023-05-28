from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.custom_event.verb import Verb
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.prep_phrase import PrepPhrase
from app.classes.custom_event.adverb import Adverb
from app.classes.custom_event.predicate import Predicate

class PrepNode(Element[PrepPhrase]):
    node_type = UnitType.PREP_PHRASE

class AdverbNode(Element[Adverb]):
    node_type = UnitType.ADVERB
    
class PredicateNode(Element[Predicate]):
    node_type = UnitType.PREDICATE
    
class DobjNode(Element[NounPhrase]):
    node_type = UnitType.DOBJ

class VerbNode(Element[Verb]):
    node_type = UnitType.VERB

class FailsToNode(Element):
    node_type = UnitType.FAILS_TO

class SubjectNode(Element[NounPhrase]):
    node_type = UnitType.SUBJECT

class CustomEventNode(Element[CustomEvent]):
    node_type = UnitType.CUSTOM_EVENT