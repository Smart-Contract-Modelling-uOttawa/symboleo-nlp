from app.classes.elements.element import Element
from app.classes.units.node_type import NodeType
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.custom_event.verb import Verb
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.prep_phrase import PrepPhrase
from app.classes.custom_event.adverb import Adverb
from app.classes.custom_event.predicate import Predicate

class PrepNode(Element[PrepPhrase]):
    node_type = NodeType.PREP_PHRASE

class AdverbNode(Element[Adverb]):
    node_type = NodeType.ADVERB
    
class PredicateNode(Element[Predicate]):
    node_type = NodeType.PREDICATE
    
class DobjNode(Element[NounPhrase]):
    node_type = NodeType.DOBJ

class VerbNode(Element[Verb]):
    node_type = NodeType.VERB

class FailsToNode(Element):
    node_type = NodeType.FAILS_TO

class SubjectNode(Element[NounPhrase]):
    node_type = NodeType.SUBJECT

class CustomEventNode(Element[CustomEvent]):
    node_type = NodeType.CUSTOM_EVENT