from typing import List, Dict
from enum import Enum
from app.classes.units.all_units import *

from app.classes.spec.point_function import TimeUnit
from app.classes.spec.sym_event import SymEvent
from app.classes.events.custom_event.custom_event import CustomEvent, ConjType

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


class BeforeDate(PatternClass):
    sequence = [PT.P_BEFORE_S, PT.DATE]
    
    def __init__(self):
        super().__init__()
        self.date_text = ''
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.date_text}'
      

class CondAEvent(EventPatternClass):
    sequence = [PT.CONDITIONAL_A, PT.EVENT]

    def __init__(self) -> None:
        super().__init__()
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.nl_event.to_text()}'
    
class CondTEvent(EventPatternClass):
    sequence = [PT.CONDITIONAL_T, PT.EVENT]

    def __init__(self) -> None:
        super().__init__()
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.nl_event.to_text()}'


class ExceptEvent(EventPatternClass):
    sequence = [PT.P_EXCEPTION, PT.EVENT]

    def __init__(self) -> None:
        super().__init__()
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.nl_event.to_text()}'


class BeforeEvent(EventPatternClass):
    sequence = [PT.P_BEFORE_WE, PT.EVENT]

    def __init__(self) -> None:
        super().__init__()
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.nl_event.to_text()}'
    

class WithinTimespanEvent(EventPatternClass):
    sequence = [PT.WITHIN, PT.TIMESPAN, PT.P_AFTER_W, PT.EVENT]

    def __init__(self) -> None:
        super().__init__()
        self.timespan_unit: TimeUnit = None
        self.timespan_value = ''
    
    def to_text(self) -> str:
        return f'within {self.timespan_value} {self.timespan_unit.value} {self.keyword} {self.nl_event.to_text(ConjType.CONTINUOUS)}'


# ...
