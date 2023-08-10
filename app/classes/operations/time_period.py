from __future__ import annotations
from typing import Dict

class TimePeriod:
    def __init__(self, s:str):
        self.time_period_str = s
    
    def __eq__(self, __value: TimePeriod) -> bool:
        return self.time_period_str == __value.time_period_str

    @property
    def start(self):
        return f'{self.time_period_str}.start'
    
    @property
    def end(self):
        return f'{self.time_period_str}.end'

    @staticmethod
    def time_period_dict() -> Dict[str, str]:
        return {
            'the contract period': 'self',
        }
    
