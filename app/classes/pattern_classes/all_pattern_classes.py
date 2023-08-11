from app.classes.pattern_classes.after_date import AfterDate
from app.classes.pattern_classes.after_event import AfterEvent
from app.classes.pattern_classes.after_timespan_after_event import AfterTimespanAfterEvent
from app.classes.pattern_classes.after_timespan_before_event import AfterTimespanBeforeEvent
from app.classes.pattern_classes.before_date import BeforeDate
from app.classes.pattern_classes.before_event import BeforeEvent
from app.classes.pattern_classes.cond_a_event import CondAEvent
from app.classes.pattern_classes.cond_t_event import CondTEvent
from app.classes.pattern_classes.except_event import ExceptEvent
from app.classes.pattern_classes.timespan_after_event import TimespanAfterEvent
from app.classes.pattern_classes.timespan_before_event import TimespanBeforeEvent
from app.classes.pattern_classes.until_date import UntilDate
from app.classes.pattern_classes.until_event import UntilEvent
from app.classes.pattern_classes.within_timespan_event import WithinTimespanEvent

from app.classes.pattern_classes.between_interval import BetweenInterval
from app.classes.pattern_classes.during_time_period import DuringTimePeriod
from app.classes.pattern_classes.for_timespan_interval import ForTimespanInterval



def get_all_pattern_classes():
    return [
        AfterDate,
        AfterEvent,
        AfterTimespanAfterEvent,
        AfterTimespanBeforeEvent,
        BeforeDate,
        BeforeEvent,
        CondAEvent,
        CondTEvent,
        ExceptEvent,
        TimespanAfterEvent,
        TimespanBeforeEvent,
        UntilDate,
        UntilEvent,
        WithinTimespanEvent,
        BetweenInterval,
        DuringTimePeriod,
        ForTimespanInterval
    ]

def temporal_classes():
    return [
        AfterDate,
        AfterEvent,
        AfterTimespanAfterEvent,
        AfterTimespanBeforeEvent,
        BeforeDate,
        BeforeEvent,
        TimespanAfterEvent,
        TimespanBeforeEvent,
        WithinTimespanEvent,
        BetweenInterval,
        DuringTimePeriod,
        ForTimespanInterval
    ]

def until_classes():
    return [       
        UntilDate,
        UntilEvent
    ]

def exception_classes():
    return [ExceptEvent]

def conditional_classes():
    return [
        CondAEvent,
        CondTEvent
    ]