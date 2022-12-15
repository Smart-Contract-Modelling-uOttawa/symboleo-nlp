from app.classes.spec.helpers import VariableDotExpression, TimeValue, TimeUnit
from app.classes.spec.sym_event import ObligationEvent, ContractEvent, PowerEvent

class SymPoint():
    def to_sym(self):
        raise NotImplementedError()

class PointExpression():
    def to_sym(self):
        raise NotImplementedError()

class PointAtom(PointExpression):
    def to_sym(self):
        raise NotImplementedError()

# Added in an effort to get rid of the main VDE
class PointVDE(PointAtom):
    def __init__(self, name: str = ''):
        self.name = name
    
    def to_sym(self):
        return self.name

# Note: Changed the arg from PointExpression to PointAtom to avoid circular dependency
class PointFunction(PointExpression):
    arg = PointAtom()
    value = TimeValue()
    unit = TimeUnit() 
    
    def __init__(self, arg: PointAtom, value: TimeValue, time_unit: TimeUnit):
        self.name = 'Date.add'
        self.arg = arg
        self.value = value
        self.time_unit = time_unit

    def to_sym(self):
        return f'{self.name}({self.arg.to_sym()}, {self.value.to_sym()}, {self.time_unit.to_sym()})'


# May be able to just replace this with the PointVDE, and make that inherit PointAtom...
# class PointAtomParameterDotExpression(PointAtom):
#     variable = PointVDE()

#     def __init__(self, variable: PointVDE):
#         self.variable = variable

#     def to_sym(self):
#         return self.variable.to_sym()


class PointAtomObligationEvent(PointAtom):
    obligation_event = ObligationEvent()

    def __init__(self, obligation_event: ObligationEvent):
        self.obligation_event = obligation_event

    def to_sym(self):
        return self.obligation_event.to_sym()


class PointAtomPowerEvent(PointAtom):
    power_event = PowerEvent()

    def __init__(self, power_event: PowerEvent):
        self.power_event = power_event

    def to_sym(self):
        return self.power_event.to_sym()


class PointAtomContractEvent(PointAtom):
    contract_event = ContractEvent()

    def __init__(self, contract_event: ContractEvent):
        self.contract_event = contract_event

    def to_sym(self):
        return self.contract_event.to_sym()


class Point(SymPoint):
    point_expression = PointExpression()

    def __init__(self, point_expression: PointExpression):
        self.point_expression = point_expression
    
    def to_sym(self):
        return self.point_expression.to_sym()


class Beginning(PointExpression):
    def to_sym(self):
        return 'MIN_DATE'

class Ending(PointExpression):
    def to_sym(self):
        return 'MAX_DATE'