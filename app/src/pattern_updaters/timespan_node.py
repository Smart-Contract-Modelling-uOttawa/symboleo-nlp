from app.classes.selection.timespan_node import TimespanNode
from app.classes.patterns.pattern import Pattern
from app.classes.patterns.all_patterns import WithinTimespanEvent

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class TimespanUpdater(IUpdatePattern):
    def update(self, node: TimespanNode, pattern: Pattern):
        if isinstance(pattern, (WithinTimespanEvent)):
            pattern.timespan = node.value
        