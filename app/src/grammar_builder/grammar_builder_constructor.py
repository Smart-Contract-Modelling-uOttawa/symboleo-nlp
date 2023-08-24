from app.src.grammar_builder.pattern_tree_builder import PatternTreeBuilder
from app.src.grammar_builder.tree_merger import TreeMerger
from app.src.grammar_builder.grammar_builder import GrammarBuilder

from app.classes.grammar.full_grammar import FULL_GRAMMAR

class GrammarBuilderConstructor:
    @staticmethod
    def construct() -> GrammarBuilder:

        pattern_tree_builder = PatternTreeBuilder(FULL_GRAMMAR)
        tree_merger = TreeMerger()

        return GrammarBuilder(
            pattern_tree_builder,
            tree_merger
        )
