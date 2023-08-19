from __future__ import annotations
from typing import Dict
from app.classes.spec.sym_point import PointExpression, PointVDE, PointAtomContractEvent
from app.classes.spec.sym_event import ContractEvent, ContractEventName

class TimePeriod:
    def __init__(self, s:str, start: PointExpression = None, end: PointExpression = None):
        self.time_period_str = s
        self.start = start or PointVDE(f'{s}.start')
        self.end = end or PointVDE(f'{s}.end')
    
    def __eq__(self, __value: TimePeriod) -> bool:
        return self.time_period_str == __value.time_period_str and \
            self.start == __value.start and \
            self.end == __value.end

    @staticmethod
    def time_period_dict() -> Dict[str, TimePeriod]:
        return {
            'the contract period': TimePeriod(
                'contract', 
                PointAtomContractEvent(ContractEvent(ContractEventName.Activated)),
                PointAtomContractEvent(ContractEvent(ContractEventName.Terminated))
            ),
        }

    