from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType
from app.classes.other.verb import Verb
from app.classes.other.noun_phrase import NounPhrase
from app.classes.other.prep_phrase import PrepPhrase
from app.classes.other.adverb import Adverb
from app.classes.other.predicate import Predicate

class PrepNode(SelectedNode[PrepPhrase]):
    node_type = NodeType.PREP_PHRASE

class AdverbNode(SelectedNode[Adverb]):
    node_type = NodeType.ADVERB
    
class PredicateNode(SelectedNode[Predicate]):
    node_type = NodeType.PREDICATE
    
class DobjNode(SelectedNode[NounPhrase]):
    node_type = NodeType.DOBJ

class VerbNode(SelectedNode[Verb]):
    node_type = NodeType.VERB

class SubjectNode(SelectedNode[NounPhrase]):
    node_type = NodeType.SUBJECT