from app.classes.units.node_type import NodeType
from app.classes.units.input_unit import InputUnit
from app.classes.elements.custom_event_node import *
from app.classes.elements.final_node import FinalNode

from app.classes.template_event.common_event import CommonEvent

class IHandleCommonEvents:
    def handle(self, evt: CommonEvent, curr: InputUnit) -> Element:
        raise NotImplementedError()
    

class CommonEventHandler(IHandleCommonEvents):
    def handle(self, evt: CommonEvent, curr: InputUnit) -> Element:
        if curr.node_type == NodeType.SUBJECT:
            if evt.subj:
                return SubjectNode(evt.subj)

        if curr.node_type == NodeType.VERB:
            return VerbNode(evt.verb)

        if curr.node_type == NodeType.DOBJ:
            return DobjNode(evt.dobj)
        
        if curr.node_type == NodeType.ADVERB:
            return AdverbNode(evt.adverb)
        
        if curr.node_type == NodeType.FINAL_NODE:
            return FinalNode(CommonEvent(common_event_key=evt.common_event_key))
        
        return None