from typing import List
from app.src.rules.shared.interfaces import IExtractProperties, IExtractPredicates


class DomainPropTestValue:
    def __init__(self, input_value:str, expected_property: List[str]):
        self.input_value = input_value
        self.expected_property = expected_property


class ContractSpecTestValue:
    def __init__(self, input_value:str, expected_sym: List[str], key = ''):
        self.input_value = input_value
        self.expected_sym = expected_sym
        self.key = key


class DomainPropTestSuite:
    def __init__(
        self,
        key: str,
        sut: IExtractProperties,
        test_suite: List[DomainPropTestValue]
    ):
        self.key = key
        self.sut = sut
        self.test_suite = test_suite


class ContractSpecTestSuite:
    def __init__(
        self,
        key: str,
        sut: IExtractPredicates,
        test_suite: List[ContractSpecTestValue]
    ):
        self.key = key
        self.sut = sut
        self.test_suite = test_suite