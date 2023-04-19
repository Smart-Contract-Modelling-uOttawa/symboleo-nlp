from app.classes.spec.sym_event import SymEvent
from app.classes.spec.sym_point import SymPoint
from app.classes.spec.sym_interval import SymInterval
from app.classes.spec.sym_situation import SymSituation

class PredicateFunction:
    def to_sym(self):
        raise NotImplementedError()


class PredicateFunctionHappens(PredicateFunction):
    event = SymEvent()

    def __init__(self, event: SymEvent):
        self.event = event
    
    def to_sym(self):
        return f'Happens({self.event.to_sym()})'


class PredicateFunctionWHappensBefore(PredicateFunctionHappens):
    point = SymPoint()

    def __init__(self, event: SymEvent, point: SymPoint):
        self.name = 'WhappensBefore'
        self.event = event
        self.point = point
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.point.to_sym()})'


class PredicateFunctionSHappensBefore(PredicateFunctionHappens):
    point = SymPoint()

    def __init__(self, event: SymEvent, point: SymPoint):
        self.name = 'SHappensBefore'
        self.event = event
        self.point = point
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.point.to_sym()})'


class PredicateFunctionHappensWithin(PredicateFunctionHappens):
    event = SymEvent()
    interval = SymInterval()

    def __init__(self, event: SymEvent, interval: SymInterval):
        self.name = 'HappensWithin'
        self.event = event
        self.interval = interval
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.interval.to_sym()})'


class PredicateFunctionWHappensBeforeEvent(PredicateFunctionHappens):
    event2 = SymEvent()

    def __init__(self, event: SymEvent, event2: SymEvent):
        self.name = 'WhappensBeforeE'
        self.event = event
        self.event2 = event2
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.event2.to_sym()})'


class PredicateFunctionSHappensBeforeEvent(PredicateFunctionHappens):
    event2 = SymEvent()

    def __init__(self, event: SymEvent, event2: SymEvent):
        self.name = 'ShappensBeforeE'
        self.event = event
        self.event2 = event2
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.event2.to_sym()})'


class PredicateFunctionHappensAfter(PredicateFunction):
    point = SymPoint()

    def __init__(self, event: SymEvent, point: SymPoint):
        self.name = 'HappensAfter'
        self.event = event
        self.point = point
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.point.to_sym()})'


class PredicateFunctionOccurs(PredicateFunction):
    situation = SymSituation()
    interval = SymInterval()

    def __init__(self, situation: SymSituation, interval: SymInterval):
        self.name = 'Occurs'
        self.situation = situation
        self.interval = interval
    
    def to_sym(self):
        return f'{self.name}({self.situation.to_sym()}, {self.interval.to_sym()})'

