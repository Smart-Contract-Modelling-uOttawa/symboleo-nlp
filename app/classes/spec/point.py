from app.classes.spec.helpers import VariableDotExpression, TimeValue
from app.classes.spec.sym_event import ObligationEvent, ContractEvent, PowerEvent

class PointExpression():
    def to_sym(self):
        raise NotImplementedError()

# circular...
class PointFunction(PointExpression):
    def __init__(self, arg: PointExpression, value: TimeValue, time_unit: str):
        self.name = 'Date.add'
        self.arg = arg
        self.value = value
        self.time_unit = time_unit

    def to_sym(self):
        return f'{self.name}({self.arg.to_sym()}, {self.value.to_sym()}, {self.time_unit})'


class PointAtom(PointExpression):
    def to_sym(self):
        raise NotImplementedError()


class PointAtomParameterDotExpression(PointAtom):
    def __init__(self, variable: VariableDotExpression):
        self.variable = variable

    def to_sym(self):
        return self.variable.to_sym()


class PointAtomObligationEvent(PointAtom):
    def __init__(self, obligation_event: ObligationEvent):
        self.obligation_event = obligation_event

    def to_sym(self):
        return self.obligation_event.to_sym()


class PointAtomPowerEvent(PointAtom):
    def __init__(self, power_event: PowerEvent):
        self.power_event = power_event

    def to_sym(self):
        return self.power_event.to_sym()


class PointAtomContractEvent(PointAtom):
    def __init__(self, contract_event: ContractEvent):
        self.contract_event = contract_event

    def to_sym(self):
        return self.contract_event.to_sym()


class Point():
    def __init__(self, point_expression: PointExpression):
        self.point_expression = point_expression
    
    def to_sym(self):
        return self.point_expression.to_sym()
