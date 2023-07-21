from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import VariableEvent
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

from app.src.custom_event_extractor.custom_event_extractor import IExtractCustomEvents

class CustomEventFiller(IFillPatternUnit):
    def __init__(self, event_extractor:IExtractCustomEvents):
        self.__event_extractor = event_extractor

    def fill(self, pattern_class: EventPatternClass, contract: SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        nl_event = self.__event_extractor.extract(input_list, contract)
        result.event = VariableEvent(nl_event.event_key())
        result.nl_event = nl_event
        
        return result