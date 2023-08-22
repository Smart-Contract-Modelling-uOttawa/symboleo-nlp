from typing import List, Dict
from app.classes.pattern_classes.pattern_variables import PatternVariable

from app.classes.spec.sym_event import SymEvent
from app.classes.events.custom_event.custom_event import CustomEvent

class PatternClass:
    sequence: List[PatternVariable] = []

    def __init__(self, val_dict = None) -> None:
        self.keyword = ''
        self.val_dict: Dict[PatternVariable, str] = val_dict or {}

    def to_text(self) -> str:
        pv_list = [self.val_dict[x] for x in self.sequence]
        return ' '.join(pv_list)


class EventPatternClass(PatternClass):
    def __init__(self, val_dict = None) -> None:
        super().__init__(val_dict)
        self.event: SymEvent = None
        self.nl_event: CustomEvent = None

