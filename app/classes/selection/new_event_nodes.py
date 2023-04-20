from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

from app.classes.other.verb import Verb
from app.classes.other.subject import Subject
from app.classes.other.prep_phrase import PrepPhrase

class PrepNode(SelectedNode[PrepPhrase]):
    node_type = NodeType.PREP_PHRASE

class AdverbNode(SelectedNode[str]):
    node_type = NodeType.ADVERB
    
class PredicateNode(SelectedNode[str]):
    node_type = NodeType.PREDICATE
    
class DobjNode(SelectedNode[str]):
    node_type = NodeType.DOBJ

class VerbNode(SelectedNode[Verb]):
    node_type = NodeType.VERB

class SubjectNode(SelectedNode[Subject]):
    node_type = NodeType.SUBJECT