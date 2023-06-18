from typing import List
import copy
from app.classes.spec.sym_event import VariableEvent
from app.classes.operations.user_input import UserInput
from app.classes.patterns.pattern_classes import PatternClass, EventPatternClass
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

# Will need the event extractor here...
class CustomEventFiller(IFillPatternUnit):
    def fill(self, pattern_class: EventPatternClass, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        result.event = VariableEvent(input_list[i].value) # custom_event will need to be assigned a name at some point
        return result