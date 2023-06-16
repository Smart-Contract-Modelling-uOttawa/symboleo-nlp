from typing import DefaultDict, Dict, Type

from app.classes.patterns.pattern_classes import *

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates
from app.src.norm_update_extractor.handlers.before_date_handler import BeforeDateHandler
from app.src.norm_update_extractor.handlers.within_timespan_handler import WithinTimespanHandler
from app.src.norm_update_extractor.handlers.cond_a_event_handler import CondAEventHandler
from app.src.norm_update_extractor.handlers.cond_t_event_handler import CondTEventHandler
from app.src.norm_update_extractor.handlers.except_event_handler import ExceptEventHandler

class NormUpdateHandlerDictBuilder:
    @staticmethod
    def build() -> Dict[Type, IHandleNormUpdates]:
        d = {}
        d[BeforeDate] = BeforeDateHandler()
        d[WithinTimespanEvent] = WithinTimespanHandler()
        d[CondAEvent] = CondAEventHandler()
        d[CondTEvent] = CondTEventHandler()
        d[ExceptEvent] = ExceptEventHandler()
        return d
