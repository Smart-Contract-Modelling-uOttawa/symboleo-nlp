from typing import List
from app.classes.pattern_classes.pattern_variables import PatternVariable

from app.classes.spec.sym_event import SymEvent
from app.classes.events.custom_event.custom_event import CustomEvent


class PatternClass:
    sequence: List[PatternVariable]

    def __init__(self) -> None:
        self.keyword = ''

    def is_complete(self):
        return True # Will fill this one in...
    
    def to_text(self) -> str:
        return '...'


class EventPatternClass(PatternClass):
    def __init__(self) -> None:
        super().__init__()
        self.event: SymEvent = None
        self.nl_event: CustomEvent = None