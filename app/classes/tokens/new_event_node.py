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
    node_type = NodeType.PREP_PHRASE
    sn_type = PrepTarget
    prompt = 'Preposition'
    needs_value = True

class AdverbNode(AbstractNode):
    node_type = NodeType.ADVERB
    sn_type = AdverbTarget
    prompt = 'Adverb'
    children = [PrepNode]
    needs_value = True

class PredicateNode(AbstractNode):
    node_type = NodeType.PREDICATE
    sn_type = PredicateTarget
    prompt = 'Predicate'
    children = [AdverbNode]
    needs_value = True

class DobjNode(AbstractNode):
    node_type = NodeType.DOBJ
    sn_type = DobjTarget
    prompt = 'Direct Object'
    children = [AdverbNode]
    needs_value = True

class VerbNode(AbstractNode):
    node_type = NodeType.VERB
    sn_type = VerbTarget
    prompt = 'Verb'
    children = [DobjNode, AdverbNode, PredicateNode]
    needs_value = True

class SubjectNode(AbstractNode):
    node_type = NodeType.SUBJECT
    sn_type = SubjectTarget
    prompt = 'Subject'
    children = [VerbNode]
    needs_value = True

class NewEventNode(AbstractNode):
    node_type = NodeType.NEW_EVENT
    sn_type = NewEventNodeTarget
    prompt = 'New event'
    children = [SubjectNode]

