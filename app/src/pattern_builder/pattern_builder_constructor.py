from app.classes.operations.dependencies import Dependencies
from app.src.pattern_builder.pattern_class_filler import PatternClassFiller
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor
from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.pattern_builder.pattern_class_builder import PatternClassBuilder
from app.src.pattern_builder.single_pattern_checker import SinglePatternChecker
from app.src.pattern_builder.recursive_pattern_checker import RecursivePatternChecker
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler_dict import PatternUnitFillerDictConstructor

from app.classes.grammar.full_grammar import FULL_GRAMMAR

class PatternBuilderConstructor:
    @staticmethod
    def construct(deps: Dependencies) -> PatternClassBuilder:
        pattern_class_getter = AllPatternClassGetter()
        recursive_pattern_checker = RecursivePatternChecker(FULL_GRAMMAR)
        single_pattern_checker = SinglePatternChecker(recursive_pattern_checker, FULL_GRAMMAR)
        pattern_class_extractor = PatternClassExtractor(pattern_class_getter, single_pattern_checker)
        pattern_filler_dict= PatternUnitFillerDictConstructor.build(deps)
        pattern_class_filler = PatternClassFiller(pattern_filler_dict)
        pattern_class_builder = PatternClassBuilder(pattern_class_extractor, pattern_class_filler)

        return pattern_class_builder
