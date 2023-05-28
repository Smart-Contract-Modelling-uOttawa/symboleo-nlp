from typing import List
from app.classes.elements.element import Element
from app.classes.patterns.pattern import Pattern
from app.src.pattern_updaters.all_patterns_getter import IGetAllPatterns
from app.src.pattern_updaters.inner_pattern_checker import IInnerPatternChecker

class IGetPattern:
    def get_pattern(self, elements: List[Element]) -> Pattern:
        raise NotImplementedError()

class PatternGetter(IGetPattern):
    def __init__(
            self, 
            all_patterns_getter: IGetAllPatterns,
            inner_checker: IInnerPatternChecker,
        ):
        self.__all_patterns_getters = all_patterns_getter
        self.__inner_checker = inner_checker

    def get_pattern(self, elements: List[Element]) -> Pattern:
        patterns = []
        all_patterns = self.__all_patterns_getters.get()
        for pattern in all_patterns:
            res = self.__inner_checker.check_pattern(elements, pattern.sequence)
            if res:
                patterns.append(pattern
                                )
        
        if len(patterns) > 1:
            pattern_list = ','.join([str(type(x)) for x in patterns])
            raise ValueError(f'Too many potential patterns: {pattern_list}')
        if len(patterns) == 0:
            raise ValueError('No patterns found')
        return patterns[0]   
