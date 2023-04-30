from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType
from app.classes.tokens.final_node import FinalNode

from app.classes.selection.custom_event_node import CustomEventNode as CustomEventNodeTarget
from app.classes.selection.custom_event_node import SubjectNode as SubjectTarget, \
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
    children = [FinalNode]

class AdverbNode(AbstractNode):
    node_type = NodeType.ADVERB
    sn_type = AdverbTarget
    prompt = 'Adverb'
    children = [PrepNode, FinalNode]
    needs_value = True

class PredicateNode(AbstractNode):
    node_type = NodeType.PREDICATE
    sn_type = PredicateTarget
    prompt = 'Predicate'
    children = [AdverbNode, FinalNode]
    needs_value = True

class DobjNode(AbstractNode):
    node_type = NodeType.DOBJ
    sn_type = DobjTarget
    prompt = 'Direct Object'
    children = [AdverbNode, FinalNode]
    needs_value = True

class VerbNode(AbstractNode):
    node_type = NodeType.VERB
    sn_type = VerbTarget
    prompt = 'Verb'
    children = [DobjNode, AdverbNode, PredicateNode, FinalNode]
    needs_value = True

class SubjectNode(AbstractNode):
    node_type = NodeType.SUBJECT
    sn_type = SubjectTarget
    prompt = 'Subject'
    children = [VerbNode]
    needs_value = True

class CustomEventNode(AbstractNode):
    node_type = NodeType.CUSTOM_EVENT
    sn_type = CustomEventNodeTarget
    prompt = 'Custom event'
    children = [SubjectNode]

