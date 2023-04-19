from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.selection.new_event_node import NewEventNode as NewEventNodeTarget
from app.classes.selection.new_event_nodes import SubjectNode as SubjectTarget, \
    VerbNode as VerbTarget, \
    PrepNode as PrepTarget, \
    AdverbNode as AdverbTarget, \
    PredicateNode as PredicateTarget, \
    DobjNode as DobjTarget


class PrepNode(AbstractNode):
    #node_type = NodeType.PREPOSITION
    sn_type = PrepTarget
    prompt = 'Preposition'

class AdverbNode(AbstractNode):
    #node_type = NodeType.ADVERB
    sn_type = AdverbTarget
    prompt = 'Adverb'
    children = [PrepNode]

class PredicateNode(AbstractNode):
    #node_type = NodeType.PREDICATE
    sn_type = PredicateTarget
    prompt = 'Predicate'
    children = [AdverbNode]

class DobjNode(AbstractNode):
    #node_type = NodeType.DOBJ
    sn_type = DobjTarget
    prompt = 'Direct Object'
    children = [AdverbNode]

class VerbNode(AbstractNode):
    node_type = NodeType.VERB
    sn_type = VerbTarget
    prompt = 'Subject'
    children = [DobjNode, AdverbNode, PredicateNode]

class SubjectNode(AbstractNode):
    node_type = NodeType.SUBJECT
    sn_type = SubjectTarget
    prompt = 'Subject'
    children = [VerbNode]

class NewEventNode(AbstractNode):
    node_type = NodeType.NEW_EVENT
    sn_type = NewEventNodeTarget
    prompt = 'New event'
    children = [SubjectNode]

