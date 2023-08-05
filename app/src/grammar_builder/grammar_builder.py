from typing import List, Type
from copy import deepcopy

from app.classes.grammar.grammar_node import GrammarNode
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.all_pattern_classes import *
from app.src.grammar_builder.pattern_tree_builder import IBuildPatternTrees
from app.src.grammar_builder.tree_merger import IMergeTrees
        
class IBuildGrammar:
    def build(self, pattern_classes: List[PatternClass]) -> GrammarNode:
        raise NotImplementedError()


class GrammarBuilder(IBuildGrammar):
    def __init__(
            self, 
            pattern_tree_builder: IBuildPatternTrees,
            tree_merger: IMergeTrees
        ):
        self.__pattern_tree_builder = pattern_tree_builder
        self.__tree_merger = tree_merger


    def build(self, pattern_classes: List[Type[PatternClass]]) -> GrammarNode:
        curr_tree = GrammarNode('ROOT')

        for pc in pattern_classes:
            next_trees = self.__pattern_tree_builder.build(pc)
            for next_tree in next_trees:
                self.__tree_merger.merge(curr_tree, next_tree)
                curr_tree = deepcopy(curr_tree)

        return curr_tree
    