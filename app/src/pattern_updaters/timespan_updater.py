from app.classes.elements.time_elements import TimespanElement
from app.classes.patterns.pattern import Pattern
from app.classes.patterns.all_patterns import WithinTimespanEvent

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class TimespanUpdater(IUpdatePattern):
    def update(self, element: TimespanElement, pattern: Pattern):
        if isinstance(pattern, (WithinTimespanEvent)):
            pattern.timespan = element.value
        