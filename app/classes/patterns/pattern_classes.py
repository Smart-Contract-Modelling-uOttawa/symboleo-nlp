from typing import List, Dict
from enum import Enum
from app.classes.units.all_units import *

from app.classes.spec.sym_event import SymEvent

class PT(Enum):
    DATE = 'DATE'
    EVENT = 'EVENT'
    TIMESPAN = 'TIMESPAN'

    P_BEFORE_S = 'P_BEFORE_S'
    P_BEFORE_WE = 'P_BEFORE_WE'
    P_AFTER_W = 'P_AFTER_W'

    IF = 'IF'
    WITHIN = 'WITHIN'
    

pt_value_dict: Dict[PT, List[UnitType]] = {
    PT.P_BEFORE_S: [UnitType.BEFORE], #...
    PT.P_BEFORE_WE: [UnitType.BEFORE], #...
    PT.P_AFTER_W: [UnitType.OF, UnitType.AFTER], #...
    
    PT.WITHIN: [UnitType.WITHIN],
    PT.IF: [UnitType.IF],

    PT.EVENT: [UnitType.EVENT],
    PT.DATE: [UnitType.DATE],
    PT.TIMESPAN: [UnitType.TIMESPAN]
}


class PatternClass:
    sequence: List[PT]

    def is_complete(self):
        return True # Will fill this one in...


class EventPatternClass(PatternClass):
    def __init__(self) -> None:
        self.event: SymEvent = None


class BeforeDate(PatternClass):
    sequence = [PT.P_BEFORE_S, PT.DATE]
    
    def __init__(self):
        self.date_text = ''

class IfEvent(EventPatternClass):
    sequence = [PT.IF, PT.EVENT]
    

class BeforeEvent(EventPatternClass):
    sequence = [PT.P_BEFORE_WE, PT.EVENT]


class WithinTimespanEvent(EventPatternClass):
    sequence = [PT.WITHIN, PT.TIMESPAN, PT.P_AFTER_W, PT.EVENT]

    def __init__(self) -> None:
        super().__init__()
        self.timespan_unit = ''
        self.timespan_value = ''


# ...
