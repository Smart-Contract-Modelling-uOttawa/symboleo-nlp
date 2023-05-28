from typing import List, Dict, Type
from app.classes.elements.element import Element
from app.classes.patterns.pattern import Pattern

from app.src.pattern_updaters.pattern_getter import IGetPattern
from app.src.pattern_updaters.pattern_updater import IUpdatePattern

class IBuildPatterns:
    def build(self, elements: List[Element]) -> Pattern:
        raise NotImplementedError()

class PatternBuilder(IBuildPatterns):
    def __init__(
        self, 
        pattern_getter: IGetPattern,
        updater_dict: Dict[Type[Element], IUpdatePattern]
    ):
        self.__pattern_getter = pattern_getter
        self.__updater_dict = updater_dict


    def build(self, elements: List[Element]) -> Pattern:
        pattern = self.__pattern_getter.get_pattern(elements)

        for element in elements:
            updater = self.__updater_dict[type(element)]
            updater.update(element, pattern)
        
        return pattern
