from app.classes.spec.point import PointExpression
from app.classes.spec.situation import Situation

class IntervalExpression:
    def to_sym(self):
        raise NotImplementedError()
    

class IntervalFunction(IntervalExpression):
    def __init__(self, arg1:PointExpression, arg2:PointExpression):
        self.arg1 = arg1
        self.arg2 = arg2

    def to_sym(self):
        return f'Interval({self.arg1.to_sym()}, {self.arg2.to_sym()}'

# custom
class EmptyInterval(IntervalExpression):
    def to_sym(self):
        return 'X'

# circular?
class SituationExpression(IntervalExpression):
    def __init__(self, situation: Situation):
        self.situation = situation
    
    def to_sym(self):
        return self.situation.to_sym()


class Interval:
    def __init__(self, interval_expression: IntervalExpression):
        self.interval_expression = interval_expression
    
    def to_sym(self):
        return self.interval_expression.to_sym()
