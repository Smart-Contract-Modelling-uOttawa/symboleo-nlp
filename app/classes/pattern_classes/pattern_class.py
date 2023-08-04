from typing import List
from enum import Enum
from app.classes.pattern_classes.pattern_variables import PatternVariable

from app.classes.spec.sym_event import SymEvent, PowerEvent, ObligationEvent
from app.classes.events.custom_event.custom_event import CustomEvent

class PatternClass:
    sequence: List[PatternVariable] = []

    def __init__(self, val_dict = None) -> None:
        self.keyword = ''
        self.val_dict = val_dict or {}

    def to_text(self) -> str:
        pv_list = [self.val_dict[x] for x in self.sequence]
        str_list = [s for pv in pv_list for s in pv]
        return ' '.join(str_list)


class EventPatternClass(PatternClass):
    def __init__(self, val_dict = None) -> None:
        super().__init__(val_dict)
        self.event: SymEvent = None
        self.nl_event: CustomEvent = None

    def to_text(self) -> str:
        # If its a norm event, then replace with the nl_event...
        if isinstance(self.event, (PowerEvent, ObligationEvent)):
            self.val_dict[PatternVariable.EVENT] = self.nl_event.to_text().split(' ')
        
        return super().to_text()
