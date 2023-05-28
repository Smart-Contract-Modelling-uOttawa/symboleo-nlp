from app.classes.elements.element import Element
from app.classes.patterns.pattern import Pattern

class IUpdatePattern:
    def update(self, node: Element, pattern: Pattern):
        raise NotImplementedError()

class DefaultPatternUpdater(IUpdatePattern):
    def update(self, node: Element, pattern: Pattern):
        return pattern
