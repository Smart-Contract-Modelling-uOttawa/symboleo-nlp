from typing import DefaultDict, Dict, Type

from app.classes.pattern_classes.all_pattern_classes import *

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates
from app.src.norm_update_extractor.handlers.before_date_handler import BeforeDateHandler
from app.src.norm_update_extractor.handlers.before_event_handler import BeforeEventHandler
from app.src.norm_update_extractor.handlers.within_timespan_handler import WithinTimespanHandler
from app.src.norm_update_extractor.handlers.cond_a_event_handler import CondAEventHandler
from app.src.norm_update_extractor.handlers.cond_t_event_handler import CondTEventHandler
from app.src.norm_update_extractor.handlers.except_event_handler import ExceptEventHandler
from app.src.norm_update_extractor.handlers.after_date_handler import AfterDateHandler
from app.src.norm_update_extractor.handlers.after_timespan_after_event_handler import AfterTimespanAfterEventHandler
from app.src.norm_update_extractor.handlers.after_timespan_before_event_handler import AfterTimespanBeforeEventHandler
from app.src.norm_update_extractor.handlers.timespan_after_event_handler import TimespanAfterEventHandler
from app.src.norm_update_extractor.handlers.timespan_before_event_handler import TimespanBeforeEventHandler
from app.src.norm_update_extractor.handlers.until_date_handler import UntilDateHandler
from app.src.norm_update_extractor.handlers.until_event_handler import UntilEventHandler

class NormUpdateHandlerDictBuilder:
    @staticmethod
    def build() -> Dict[Type, IHandleNormUpdates]:
        d = {}
        d[BeforeDate] = BeforeDateHandler()
        d[BeforeEvent] = BeforeEventHandler()
        d[WithinTimespanEvent] = WithinTimespanHandler()
        d[CondAEvent] = CondAEventHandler()
        d[CondTEvent] = CondTEventHandler()
        d[ExceptEvent] = ExceptEventHandler()
        d[AfterDate] = AfterDateHandler()
        d[AfterTimespanAfterEvent] = AfterTimespanAfterEventHandler()
        d[AfterTimespanBeforeEvent] = AfterTimespanBeforeEventHandler()
        d[TimespanAfterEvent] = TimespanAfterEventHandler()
        d[TimespanBeforeEvent] = TimespanBeforeEventHandler()
        d[UntilDate] = UntilDateHandler()
        d[UntilEvent] = UntilEventHandler()
        
        # TODO: Still missing (tough ones)
        # EventInterval
        # NoticeEvent
        # AfterEvent
        return d
