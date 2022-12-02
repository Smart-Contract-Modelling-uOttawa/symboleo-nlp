from app.classes.spec.sym_point import PointExpression, Beginning, Ending
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


# Added these ones - can express an interval with just a single point function (e.g. Date.add(...))
class IntervalFunctionBeginning(IntervalFunction):
    def __init__(self, arg: PointExpression):
        super(IntervalFunctionBeginning, self).__init__(Beginning(), arg)

    def to_sym(self):
        return f'Interval({self.arg1.to_sym()}, {self.arg2.to_sym()}'

class IntervalFunctionEnding(IntervalFunction):
    def __init__(self, arg: PointExpression):
        super(IntervalFunctionEnding, self).__init__(arg, Ending())

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

# Added to handle certain dynamic situations
class Never(SymInterval):
    def to_sym(self):
        return 'NEVER'