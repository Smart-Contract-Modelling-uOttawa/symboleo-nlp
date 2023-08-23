from typing import List
from app.classes.units.unit_type import UnitType 
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.operations.user_input import UserInput

from app.src.pattern_builder.single_pattern_checker import ICheckSinglePattern
from app.src.pattern_builder.pattern_class_getter import IGetAllPatternClasses

# Given a list of units, return the pattern classes that match it
class IExtractPatternClass:
    def extract(self, set_to_check: List[UserInput]) -> List[PatternClass]:
        raise NotImplementedError()
    

class PatternClassExtractor(IExtractPatternClass):
    def __init__(
        self,
        all_pattern_class_getter: IGetAllPatternClasses,
        single_pattern_checker: ICheckSinglePattern
    ):
        self.__all_pattern_class_getter = all_pattern_class_getter
        self.__single_pattern_checker = single_pattern_checker


    def extract(self, set_to_check: List[UserInput]) -> List[PatternClass]:
        result_set = []
        all_classes = self.__all_pattern_class_getter.get()
        for pattern_class in all_classes:
            next_pc = self.__single_pattern_checker.check(set_to_check, pattern_class)
            if next_pc:
                result_set.append(next_pc)

        # if len(result_set) == 0:
        #     raise ValueError('No pattern classes found')
    
        return result_set     
  