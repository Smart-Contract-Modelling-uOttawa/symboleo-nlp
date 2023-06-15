from collections import defaultdict
from typing import DefaultDict, Dict, Type

from app.classes.patterns.pattern_classes import *


from app.src.update_processor2.handlers.norm_update_handler import IHandleNormUpdates

from app.src.update_processor2.handlers.before_date_handler import BeforeDateHandler
from app.src.update_processor2.handlers.before_event_handler import BeforeEventHandler
from app.src.update_processor2.handlers.within_timespan_handler import WithinTimespanHandler
from app.src.update_processor2.handlers.if_event_handler import IfEventHandler

class NormUpdateHandlerDictBuilder:
    @staticmethod
    def build() -> Dict[Type, IHandleNormUpdates]:
        d = {}
        d[BeforeEvent] = BeforeEventHandler()
        d[BeforeDate] = BeforeDateHandler()
        d[WithinTimespanEvent] = WithinTimespanHandler()
        d[IfEvent] = IfEventHandler()
        return d
