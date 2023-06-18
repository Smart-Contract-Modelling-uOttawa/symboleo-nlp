from typing import List, Dict
from enum import Enum
from app.classes.units.all_units import *

from app.classes.spec.sym_event import SymEvent
from app.classes.events.custom_event.custom_event import CustomEvent

# Pattern Variables
class PT(Enum):
    DATE = 'DATE'
    EVENT = 'EVENT'
    TIMESPAN = 'TIMESPAN'

    P_BEFORE_S = 'P_BEFORE_S'
    P_BEFORE_WE = 'P_BEFORE_WE'
    P_AFTER_W = 'P_AFTER_W'
    P_EXCEPTION = 'P_EXECEPTION'

    CONDITIONAL_A = 'IF'
    CONDITIONAL_T = 'WHEN'

    WITHIN = 'WITHIN'
    
    

# Allowed units for pattern variables
pt_value_dict: Dict[PT, List[UnitType]] = {
    PT.P_BEFORE_S: [UnitType.BEFORE], #...
    PT.P_BEFORE_WE: [UnitType.BEFORE], #...
    PT.P_AFTER_W: [UnitType.OF, UnitType.AFTER], #...
    PT.P_EXCEPTION: [UnitType.UNLESS],
    
    PT.CONDITIONAL_T: [UnitType.WHEN],
    PT.WITHIN: [UnitType.WITHIN],
    PT.CONDITIONAL_A: [UnitType.IF],

    PT.EVENT: [UnitType.EVENT],
    PT.DATE: [UnitType.DATE],
    PT.TIMESPAN: [UnitType.TIMESPAN]
}


class PatternClass:
    sequence: List[PT]

    def is_complete(self):
        return True # Will fill this one in...
    
    def to_text(self):
        return '...'


class EventPatternClass(PatternClass):
    def __init__(self) -> None:
        self.event: SymEvent = None
        self.nl_event = CustomEvent


class BeforeDate(PatternClass):
    sequence = [PT.P_BEFORE_S, PT.DATE]
    
    def __init__(self):
        self.p_before_s = ''
        self.date_text = ''
    
    def to_text(self):
        return f'{self.p_before_s} {self.date_text}'
      

class CondAEvent(EventPatternClass):
    sequence = [PT.CONDITIONAL_A, PT.EVENT]
    
class CondTEvent(EventPatternClass):
    sequence = [PT.CONDITIONAL_T, PT.EVENT]

class ExceptEvent(EventPatternClass):
    sequence = [PT.P_EXCEPTION, PT.EVENT]

class BeforeEvent(EventPatternClass):
    sequence = [PT.P_BEFORE_WE, PT.EVENT]

class WithinTimespanEvent(EventPatternClass):
    sequence = [PT.WITHIN, PT.TIMESPAN, PT.P_AFTER_W, PT.EVENT]

    def __init__(self) -> None:
        super().__init__()
        self.timespan_unit = ''
        self.timespan_value = ''


# ...
