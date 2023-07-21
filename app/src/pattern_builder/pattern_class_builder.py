from typing import List
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass

from app.src.pattern_builder.pattern_class_filler import IFillPatternClass
from app.src.pattern_builder.pattern_class_extractor import IExtractPatternClass

class IBuildPatternClass:
    def build(self, user_input: List[UserInput], contract: SymboleoContract) -> PatternClass:
        raise NotImplementedError()


class PatternClassBuilder(IBuildPatternClass):
    def __init__(
        self,
        pattern_class_extractor: IExtractPatternClass,
        pattern_class_filler: IFillPatternClass
    ):
        self.__pattern_class_extractor = pattern_class_extractor
        self.__pattern_class_filler = pattern_class_filler

    def build(self, user_input: List[UserInput], contract: SymboleoContract) -> PatternClass:
        input_types = [x.unit_type for x in user_input]
        pattern_class = self.__pattern_class_extractor.extract(input_types)

        result = self.__pattern_class_filler.fill(pattern_class, contract, user_input)
        return result
