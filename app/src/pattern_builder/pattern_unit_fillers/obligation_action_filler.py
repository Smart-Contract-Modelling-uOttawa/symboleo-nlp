from typing import List
import copy
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName
from app.classes.operations.user_input import UserInput
from app.classes.patterns.pattern_classes import PatternClass, EventPatternClass
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

class ObligationActionFiller(IFillPatternUnit):
    def fill(self, pattern_class: EventPatternClass, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        val = input_list[i].value
        ob_event = ObligationEventName[val.capitalize()]

        if isinstance(result.event, ObligationEvent):
            result.event.event_name = ob_event
        else:
            result.event = ObligationEvent(ob_event, 'X')
        
        return result