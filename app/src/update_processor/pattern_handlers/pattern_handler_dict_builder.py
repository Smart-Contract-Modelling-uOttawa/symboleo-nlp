from collections import defaultdict
from typing import DefaultDict, Dict, Type

from app.classes.patterns.all_patterns import *
from app.src.update_processor.pattern_handlers.pattern_handler import IHandlePatterns

from app.src.update_processor.pattern_handlers.before_date_handler import BeforeDateHandler
from app.src.update_processor.pattern_handlers.before_event_handler import BeforeEventHandler
from app.src.update_processor.pattern_handlers.if_event_handler import IfEventHandler
from app.src.update_processor.pattern_handlers.within_timespan_handler import WithinTimespanHandler
from app.src.update_processor.pattern_handlers.for_timespan_following_event_handler import ForTimespanFollowingEventHandler
from app.src.update_processor.pattern_handlers.unless_event_handler import UnlessEventHandler

# Maybe I frame it as the operations, rather than the patterns
# Finite operations. Then just handle those. Multiple patterns may map to same operation...
## Probably better. We'll see...

class PatternHandlerDictBuilder:
    @staticmethod
    def build() -> Dict[Type, IHandlePatterns]:
        d = {}
        #before_pf_handler = BeforePfHandler()
        d[BeforeEvent] = BeforeEventHandler()
        d[BeforeDate] = BeforeDateHandler()
        d[WithinTimespanEvent] = WithinTimespanHandler()
        #d['BEFORE_PF'] = before_pf_handler
        d[IfEvent] = IfEventHandler()
        d[ForTimespanFollowingEvent] = ForTimespanFollowingEventHandler()
        d[UnlessEvent] = UnlessEventHandler()

        return d
