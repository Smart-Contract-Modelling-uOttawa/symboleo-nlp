from app.classes.selection.selected_node import SelectedNode
from app.classes.patterns.pattern import Pattern

class IUpdatePattern:
    def update(self, node: SelectedNode, pattern: Pattern):
        raise NotImplementedError()

class DefaultPatternUpdater(IUpdatePattern):
    def update(self, node: SelectedNode, pattern: Pattern):
        return pattern
