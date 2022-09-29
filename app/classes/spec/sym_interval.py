from app.classes.spec.sym_point import PointExpression
from app.classes.spec.sym_situation import SymSituation

class SymInterval():
    def to_sym(self):
        raise NotImplementedError()


class IntervalExpression:
    def to_sym(self):
        raise NotImplementedError()
    

class IntervalFunction(IntervalExpression):
    arg1 = PointExpression()
    arg2 = PointExpression()

    def __init__(self, arg1:PointExpression, arg2:PointExpression):
        self.arg1 = arg1
        self.arg2 = arg2

    def to_sym(self):
        return f'Interval({self.arg1.to_sym()}, {self.arg2.to_sym()}'


class SituationExpression(IntervalExpression):
    situation = SymSituation()

    def __init__(self, situation: SymSituation):
        self.situation = situation
    
    def to_sym(self):
        return self.situation.to_sym()


class Interval(SymInterval):
    interval_expression = IntervalExpression()
    
    def __init__(self, interval_expression: IntervalExpression):
        self.interval_expression = interval_expression
    
    def to_sym(self):
        return self.interval_expression.to_sym()
