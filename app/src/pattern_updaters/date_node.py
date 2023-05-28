from app.classes.elements.date_node import DateNode
from app.classes.patterns.pattern import Pattern
from app.classes.patterns.all_patterns import BeforeDate

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class DateUpdater(IUpdatePattern):
    def update(self, node: DateNode, pattern: Pattern):
        if isinstance(pattern, (BeforeDate)):
            pattern.date_text = node.value
