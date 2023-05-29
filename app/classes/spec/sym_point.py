from __future__ import annotations
from app.classes.spec.sym_event import ObligationEvent, ContractEvent, PowerEvent

class SymPoint():
    def to_sym(self):
        raise NotImplementedError()

class PointExpression():
    # PointFunction | PointAtom | StartPoint | Infinity 
    def to_sym(self):
        raise NotImplementedError()

class PointAtom(PointExpression):
    # PointVDE | PointAtomObligationEvent | PointAtomPowerEvent | PointAtomContractEvent
    def to_sym(self):
        raise NotImplementedError()


# Note: Added this in an effort to get rid of the main VDE
class PointVDE(PointAtom):
    def __init__(self, name: str = ''):
        self.name = name
    
    def __eq__(self, other: PointVDE) -> bool:
        return self.name == other.name

    def to_sym(self):
        return self.name


class PointAtomObligationEvent(PointAtom):
    obligation_event = ObligationEvent()

    def __init__(self, obligation_event: ObligationEvent):
        self.obligation_event = obligation_event

    def __eq__(self, other: PointAtomObligationEvent) -> bool:
        return self.obligation_event == other.obligation_event

    def to_sym(self):
        return self.obligation_event.to_sym()


class PointAtomPowerEvent(PointAtom):
    power_event = PowerEvent()

    def __init__(self, power_event: PowerEvent):
        self.power_event = power_event

    def __eq__(self, other: PointAtomPowerEvent) -> bool:
        return self.power_event == other.power_event

    def to_sym(self):
        return self.power_event.to_sym()


class PointAtomContractEvent(PointAtom):
    contract_event = ContractEvent()

    def __init__(self, contract_event: ContractEvent):
        self.contract_event = contract_event

    def  __eq__(self, other: PointAtomContractEvent) -> bool:
        return self.contract_event == other.contract_event

    def to_sym(self):
        return self.contract_event.to_sym()


class Point(SymPoint):
    point_expression = PointExpression()

    def __init__(self, point_expression: PointExpression):
        self.point_expression = point_expression
    
    def  __eq__(self, other: Point) -> bool:
        return self.point_expression == other.point_expression
    
    def to_sym(self):
        return self.point_expression.to_sym()

class StartPoint(PointExpression):
    def __eq__(self, other) -> bool:
        return isinstance(other, StartPoint)

    def to_sym(self):
        return 'START'
    
class Infinity(PointExpression):
    def __eq__(self, other) -> bool:
        return isinstance(other, Infinity)

    def to_sym(self):
        return 'INF'

