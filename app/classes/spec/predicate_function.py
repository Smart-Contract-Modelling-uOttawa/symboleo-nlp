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


class PredicateFunctionWHappensBefore(PredicateFunction):
    event = SymEvent()
    point = SymPoint()

    def __init__(self, event: SymEvent, point: SymPoint):
        self.name = 'WhappensBefore'
        self.event = event
        self.point = point
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.point.to_sym()})'


# class PredicateFunctionSHappensBefore(PredicateFunction):
#     event = SymEvent()
#     point = SymPoint()

#     def __init__(self, event: SymEvent, point: SymPoint):
#         self.name = 'SHappensBefore'
#         self.event = event
#         self.point = point
    
#     def to_sym(self):
#         return f'{self.name}({self.event.to_sym()}, {self.point.to_sym()})'


class PredicateFunctionHappensWithin(PredicateFunction):
    event = SymEvent()
    interval = SymInterval()

    def __init__(self, event: SymEvent, interval: SymInterval):
        self.name = 'HappensWithin'
        self.event = event
        self.interval = interval
    
    def to_sym(self):
        return f'{self.name}({self.event.to_sym()}, {self.interval.to_sym()})'


class PredicateFunctionWHappensBeforeEvent(PredicateFunction):
    event1 = SymEvent()
    event2 = SymEvent()

    def __init__(self, event1: SymEvent, event2: SymEvent):
        self.name = 'WhappensBeforeE'
        self.event1 = event1
        self.event2 = event2
    
    def to_sym(self):
        return f'{self.name}({self.event1.to_sym()}, {self.event2.to_sym()})'

# class PredicateFunctionSHappensBeforeEvent(PredicateFunction):
#     event1 = SymEvent()
#     event2 = SymEvent()

#     def __init__(self, event1: SymEvent, event2: SymEvent):
#         self.name = 'ShappensBeforeE'
#         self.event1 = event1
#         self.event2 = event2
    
#     def to_sym(self):
#         return f'{self.name}({self.event1.to_sym()}, {self.event2.to_sym()})'


class PredicateFunctionHappensAfter(PredicateFunction):
    event = SymEvent()
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

