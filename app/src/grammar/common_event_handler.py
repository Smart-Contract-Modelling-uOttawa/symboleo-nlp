from app.classes.units.unit_type import UnitType
from app.classes.units.input_unit import InputUnit
from app.classes.elements.custom_event_elements import *
from app.classes.elements.static_elements import FinalElement

from app.classes.template_event.common_event import CommonEvent

# TODO: Re-integate this

class IHandleCommonEvents:
    def handle(self, evt: CommonEvent, curr: InputUnit) -> Element:
        raise NotImplementedError()
    

class CommonEventHandler(IHandleCommonEvents):
    def handle(self, evt: CommonEvent, curr: InputUnit) -> Element:
        if curr.unit_type == UnitType.SUBJECT:
            if evt.subj:
                return SubjectElement(evt.subj)

        if curr.unit_type == UnitType.VERB:
            return VerbElement(evt.verb)

        if curr.unit_type == UnitType.DOBJ:
            return DobjElement(evt.dobj)
        
        if curr.unit_type == UnitType.ADVERB:
            return AdverbElement(evt.adverb)
        
        if curr.unit_type == UnitType.FINAL_NODE:
            return FinalElement(CommonEvent(common_event_key=evt.common_event_key))
        
        return None