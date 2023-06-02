from typing import List
from app.classes.patterns.all_patterns import *

class IGetAllPatterns:
    def get(self) -> List[Pattern]:
        raise NotImplementedError()

class AllPatternsGetter(IGetAllPatterns):
    def get(self) -> List[Pattern]:
        return [
            BeforeEvent(),
            BeforeDate(),
            WithinTimespanEvent(),
            IfEvent(),
            ForTimespanFollowingEvent(),
            UnlessEvent(),
            UntilEvent(),
            WhenEvent()
        ]
