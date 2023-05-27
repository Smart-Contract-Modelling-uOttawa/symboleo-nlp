from app.src.pattern_updaters.inner_pattern_checker import InnerPatternChecker
from app.src.pattern_updaters.pattern_getter import PatternGetter
from app.src.pattern_updaters.all_patterns_getter import AllPatternsGetter
from app.src.pattern_updaters.pattern_updater_dict import PatternUpdaterDictConstructor
from app.src.pattern_updaters.pattern_builder import PatternBuilder

# Sorry about the name...
class PatternBuilderBuilder:
    @staticmethod
    def build() -> PatternBuilder:
        all_patterns_getter = AllPatternsGetter()
        inner_checker = InnerPatternChecker()
        pattern_getter = PatternGetter(all_patterns_getter, inner_checker)
        pattern_updater = PatternUpdaterDictConstructor.build()
        pattern_builder = PatternBuilder(pattern_getter, pattern_updater)
        return pattern_builder

