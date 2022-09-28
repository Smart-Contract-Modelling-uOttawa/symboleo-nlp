from app.classes.spec.sym_event import SymEvent
from app.classes.spec.point import Point
from app.classes.spec.interval import Interval
from app.classes.spec.situation import Situation

class PredicateFunction:
    def to_sym(self):
        raise NotImplementedError()


class PredicateFunctionHappens(PredicateFunction):
    def __init__(self, event: SymEvent):
        self.event = event
    
    def to_sym(self):
        return f'Happens({self.event.to_sym()})'


class PredicateFunctionWHappensBefore(PredicateFunction):
    def __init__(self, event: SymEvent, point: Point):
        self.name = 'WhappensBefore'
        self.event = event
        self.point = point
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.point.to_sym()})'


class PredicateFunctionSHappensBefore(PredicateFunction):
    def __init__(self, event: SymEvent, point: Point):
        self.name = 'SHappensBefore'
        self.event = event
        self.point = point
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.point.to_sym()})'


class PredicateFunctionHappensWithin(PredicateFunction):
    def __init__(self, event: SymEvent, interval: Interval):
        self.name = 'HappensWithin'
        self.event = event
        self.interval = interval
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.interval.to_sym()})'


class PredicateFunctionWHappensBeforeEvent(PredicateFunction):
    def __init__(self, event1: SymEvent, event2: SymEvent):
        self.name = 'WhappensBeforeE'
        self.event1 = event1
        self.event2 = event2
    
    def to_sym(self):
        return f'{self.name}({self.event1.to_sym()}, {self.event2.to_sym()})'

class PredicateFunctionSHappensBeforeEvent(PredicateFunction):
    def __init__(self, event1: SymEvent, event2: SymEvent):
        self.name = 'ShappensBeforeE'
        self.event1 = event1
        self.event2 = event2
    
    def to_sym(self):
        return f'{self.name}({self.event1.to_sym()}, {self.event2.to_sym()})'


class PredicateFunctionHappensAfter(PredicateFunction):
    def __init__(self, event: SymEvent, point: Point):
        self.name = 'HappensAfter'
        self.event = event
        self.point = point
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.point.to_sym()})'


class PredicateFunctionOccurs(PredicateFunction):
    def __init__(self, situation: Situation, interval: Interval):
        self.name = 'Occurs'
        self.situation = situation
        self.interval = interval
    
    def to_sym(self):
        return f'{self.name}({self.situation.to_sym()}, {self.interval.to_sym()})'

