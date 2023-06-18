from typing import List
import copy
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName
from app.classes.operations.user_input import UserInput
from app.classes.patterns.pattern_classes import PatternClass, EventPatternClass
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

# May eventually need to bring in the contract here...
class ObligationSubjectFiller(IFillPatternUnit):
    def fill(self, pattern_class: EventPatternClass, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        val = input_list[i].value

        ob_val = val.split('.')[1] 

        if isinstance(result.event, ObligationEvent):
            result.event.obligation_variable = ob_val
        else:
            result.event = ObligationEvent(ObligationEventName.Activated, ob_val)

        return result