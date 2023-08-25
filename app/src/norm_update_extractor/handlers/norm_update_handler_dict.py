from typing import DefaultDict, Dict, Type

from app.classes.pattern_classes.all_pattern_classes import *

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates
from app.src.norm_update_extractor.handlers.after_event_handler import AfterEventHandler
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

from app.src.norm_update_extractor.handlers.between_interval_handler import BetweenIntervalHandler
from app.src.norm_update_extractor.handlers.for_timespan_interval_handler import ForTimespanIntervalHandler
from app.src.norm_update_extractor.handlers.during_time_period_handler import DuringTimePeriodHandler

# Helpers
from app.src.object_mappers.time_period_mapper import TimePeriodMapper
from app.src.object_mappers.timepoint_mapper import TimepointMapper
from app.src.object_mappers.date_mapper import DateMapper
from app.src.object_mappers.timespan_mapper import TimespanMapper

class NormUpdateHandlerDictBuilder:
    @staticmethod
    def build() -> Dict[Type, IHandleNormUpdates]:


        time_period_mapper = TimePeriodMapper()
        timepoint_mapper = TimepointMapper()
        timespan_mapper = TimespanMapper()
        date_mapper = DateMapper()


        d = {}
        d[BeforeDate] = BeforeDateHandler(date_mapper)
        d[BeforeEvent] = BeforeEventHandler()
        d[WithinTimespanEvent] = WithinTimespanHandler(timespan_mapper)
        d[CondAEvent] = CondAEventHandler()
        d[CondTEvent] = CondTEventHandler()
        d[ExceptEvent] = ExceptEventHandler()
        d[AfterDate] = AfterDateHandler(date_mapper)
        d[AfterEvent] = AfterEventHandler()
        d[AfterTimespanAfterEvent] = AfterTimespanAfterEventHandler(timespan_mapper)
        d[AfterTimespanBeforeEvent] = AfterTimespanBeforeEventHandler(timespan_mapper)
        d[TimespanAfterEvent] = TimespanAfterEventHandler(timespan_mapper)
        d[TimespanBeforeEvent] = TimespanBeforeEventHandler(timespan_mapper)
        d[UntilDate] = UntilDateHandler(date_mapper)
        d[UntilEvent] = UntilEventHandler()

        d[DuringTimePeriod] = DuringTimePeriodHandler(time_period_mapper)
        d[ForTimespanInterval] = ForTimespanIntervalHandler(timepoint_mapper, timespan_mapper)
        d[BetweenInterval] = BetweenIntervalHandler(date_mapper)

        return d
