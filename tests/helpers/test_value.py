from typing import List

class DomainPropTestValue:
    def __init__(self, input_value:str, expected_property: List[str]):
        self.input_value = input_value
        self.expected_property = expected_property


class ContractSpecTestValue:
    def __init__(self, input_value:str, expected_sym: List[str], key = ''):
        self.input_value = input_value
        self.expected_sym = expected_sym
        self.key = key

