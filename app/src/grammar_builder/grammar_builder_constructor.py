from app.src.grammar_builder.pattern_tree_builder import PatternTreeBuilder
from app.src.grammar_builder.tree_merger import TreeMerger
from app.src.grammar_builder.grammar_builder import GrammarBuilder
        
class GrammarBuilderConstructor:
    @staticmethod
    def construct() -> GrammarBuilder:

        pattern_tree_builder = PatternTreeBuilder()
        tree_merger = TreeMerger()

        return GrammarBuilder(
            pattern_tree_builder,
            tree_merger
        )
