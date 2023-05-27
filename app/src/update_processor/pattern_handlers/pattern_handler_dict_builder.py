from collections import defaultdict
from typing import DefaultDict, Dict, Type

from app.classes.frames.all_frames import *
from app.src.update_processor.pattern_handlers.pattern_handler import IHandlePatterns

from app.src.update_processor.pattern_handlers.before_date_handler import BeforeDateHandler
from app.src.update_processor.pattern_handlers.before_event_handler import BeforeEventHandler
from app.src.update_processor.pattern_handlers.before_pf_handler import BeforePfHandler
from app.src.update_processor.pattern_handlers.if_event_handler import IfEventHandler
from app.src.update_processor.pattern_handlers.within_timespan_handler import WithinTimespanHandler

# Maybe I frame it as the operations, rather than the patterns
# Finite operations. Then just handle those. Multiple patterns may map to same operation...
## Probably better. We'll see...

class PatternHandlerDictBuilder:
    @staticmethod
    def build() -> Dict[Type, IHandlePatterns]:
        d = {}
        #before_pf_handler = BeforePfHandler()
        # Will replace pasttern_key with the frame type...
        d[BeforeEventFrame] = BeforeEventHandler()
        d[BeforeDateFrame] = BeforeDateHandler()
        d[WithinTimespanEventFrame] = WithinTimespanHandler()
        #d['BEFORE_PF'] = before_pf_handler
        d[IfEventFrame] = IfEventHandler()

        return d
