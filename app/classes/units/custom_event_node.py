from app.classes.units.input_unit import InputUnit
from app.classes.units.node_type import NodeType
from app.classes.units.final_node import FinalNode

from app.classes.elements.custom_event_node import CustomEventNode as CustomEventNodeTarget
from app.classes.elements.custom_event_node import SubjectNode as SubjectTarget, \
    VerbNode as VerbTarget, \
    PrepNode as PrepTarget, \
    AdverbNode as AdverbTarget, \
    PredicateNode as PredicateTarget, \
    DobjNode as DobjTarget


class PrepNode(InputUnit):
    node_type = NodeType.PREP_PHRASE
    sn_type = PrepTarget
    prompt = 'Preposition'
    needs_value = True
    children = [FinalNode]

class AdverbNode(InputUnit):
    node_type = NodeType.ADVERB
    sn_type = AdverbTarget
    prompt = 'Adverb'
    children = [PrepNode, FinalNode]
    needs_value = True

class PredicateNode(InputUnit):
    node_type = NodeType.PREDICATE
    sn_type = PredicateTarget
    prompt = 'Predicate'
    children = [AdverbNode, FinalNode]
    needs_value = True

class DobjNode(InputUnit):
    node_type = NodeType.DOBJ
    sn_type = DobjTarget
    prompt = 'Direct Object'
    children = [AdverbNode, FinalNode]
    needs_value = True

class VerbNode(InputUnit):
    node_type = NodeType.VERB
    sn_type = VerbTarget
    prompt = 'Verb'
    children = [DobjNode, AdverbNode, PredicateNode, FinalNode]
    needs_value = True

class SubjectNode(InputUnit):
    node_type = NodeType.SUBJECT
    sn_type = SubjectTarget
    prompt = 'Subject'
    children = [VerbNode]
    needs_value = True

class CustomEventNode(InputUnit):
    node_type = NodeType.CUSTOM_EVENT
    sn_type = CustomEventNodeTarget
    prompt = 'Custom event'
    children = [SubjectNode]

