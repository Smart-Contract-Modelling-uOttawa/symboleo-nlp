from app.classes.operations.dependencies import Dependencies
from app.src.pattern_builder.pattern_class_filler import PatternClassFiller
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor
from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.pattern_builder.pattern_class_builder import PatternClassBuilder
from app.src.pattern_builder.single_pattern_checker2 import SinglePatternChecker2
from app.src.pattern_builder.recursive_pattern_checker import RecursivePatternChecker
from app.src.operations.pattern_class_resolver import PatternClassResolver
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler_dict import PatternUnitFillerDictConstructor

class PatternBuilderConstructor:
    @staticmethod
    def construct(deps: Dependencies) -> PatternClassBuilder:
        pattern_class_getter = AllPatternClassGetter()
        recursive_pattern_checker = RecursivePatternChecker()
        single_pattern_checker = SinglePatternChecker2(recursive_pattern_checker)
        pattern_class_extractor = PatternClassExtractor(pattern_class_getter, single_pattern_checker)
        pattern_filler_dict= PatternUnitFillerDictConstructor.build(deps)
        pattern_class_filler = PatternClassFiller(pattern_filler_dict)
        pattern_class_builder = PatternClassBuilder(pattern_class_extractor, pattern_class_filler)

        return pattern_class_builder
