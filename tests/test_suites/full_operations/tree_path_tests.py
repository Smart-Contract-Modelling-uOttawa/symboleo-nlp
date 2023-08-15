import unittest
from unittest.mock import MagicMock
from typing import List

from app.classes.grammar.grammar_node import GrammarNode
from app.classes.units.unit_type import UnitType
from app.classes.operations.user_input import UserInput
from app.src.grammar_builder.grammar_builder_constructor import GrammarBuilderConstructor
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor
from app.src.pattern_builder.single_pattern_checker2 import SinglePatternChecker2
from app.src.pattern_builder.recursive_pattern_checker import RecursivePatternChecker
from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter


# Parse every tree path, and ensure its a valid CNL pattern
# May move to full test folder
class TreePathTests(unittest.TestCase):
    def setUp(self):
        self.grammar = GrammarBuilderConstructor.construct()

    def test_tree_paths(self):

        getter = AllPatternClassGetter()
        all_pcs = getter.get()
        gb = GrammarBuilderConstructor.construct()

        recursive_checker = RecursivePatternChecker()
        single_checker = SinglePatternChecker2(recursive_checker)
        pattern_extractor = PatternClassExtractor(getter, single_checker)

        grammar_tree = gb.build(all_pcs)

        tp = TreeParser()
        all_paths = tp.traverse_tree_paths(grammar_tree)
        # print(len(all_paths))

        for path in all_paths:
            units = [UnitType[p] for p in path[1:]]
            user_inputs = [UserInput(x, '') for x in units]
            pcs = pattern_extractor.extract(user_inputs)
            self.assertTrue(len(pcs) > 0)


class TreeParser:
    def __init__(self):
        self.all_paths = []

    def traverse_tree_paths(self, root: GrammarNode):
        self.all_paths = []
        self._dfs(root, [])
        return self.all_paths

    def _dfs(self, node: GrammarNode, current_path: List[GrammarNode]):
        if not node.children:
            self.all_paths.append(current_path + [node.name])
        else:
            current_path.append(node.name)
            for child in node.children:
                self._dfs(child, current_path)
            current_path.pop()

if __name__ == '__main__':
    unittest.main()
