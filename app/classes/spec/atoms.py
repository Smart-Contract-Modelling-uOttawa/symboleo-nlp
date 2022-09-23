
from app.classes.spec.symboleo_spec import Atom
from app.classes.spec.helpers import Point, SymEvent, Situation, Interval

class EventProposition(Atom):
    # define a Point
    def __init__(self, event: SymEvent, point: Point):
        self.event = event
        self.point = point
    
    def to_sym(self):
        event_text = self.event.to_sym()
        point_text = self.point.to_sym()
        return f'happens({event_text}, {point_text})'
    

class SituationProposition(Atom):
    def __init__(self, situation: Situation, interval: Interval):
        self.situation = situation
        self.interval = interval
    
    def to_sym(self):
        situation_text = self.situation.to_sym()
        interval_text = self.interval.to_sym()
        return f'occurs({situation_text}, {interval_text})'


class ShorthandAtom(Atom):
    def __init__(self, short_name: str):
        self.short_name = short_name
        ## ???
    
    def to_sym(self):
        ## ???
        raise NotImplementedError()

class WithinAtom(Atom):
    def __init__(self, point: Point, interval: Interval):
        self.point = point
        self.interval = interval
    
    def to_sym(self):
        point_text = self.point.to_sym()
        interval_text = self.interval.to_sym()
        return f'{point_text} within {interval_text}'

### More Atoms...

