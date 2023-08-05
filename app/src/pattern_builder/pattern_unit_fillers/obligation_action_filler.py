from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

class ObligationActionFiller(IFillPatternUnit):
    def fill(self, pattern_class: EventPatternClass, contract: SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        val = input_list[i].value
        ob_event = ObligationEventName[val.capitalize()]

        if isinstance(result.event, ObligationEvent):
            result.event.event_name = ob_event
        else:
            result.event = ObligationEvent(ob_event, 'X')
        
        if result.nl_event:
            result.nl_event.negation = (ob_event in [ObligationEventName.Violated])

        return result