from typing import List, Type

from app.classes.grammar.grammar_node import GrammarNode
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.grammar.pattern_values import full_grammar, UnitType, GOr, GAnd

# Make a function here...
from app.classes.pattern_classes.all_pattern_classes import *

class IBuildPatternTrees:
    def build(self, pattern_class: Type[PatternClass]) -> List[GrammarNode]:
        raise NotImplementedError()


class PatternTreeBuilder(IBuildPatternTrees):
    def build(self, pattern_class: Type[PatternClass]) -> List[GrammarNode]:
        next_c: List[GrammarNode] = []
        
        for x in reversed(pattern_class.sequence):
            next_c = self._handle_grammar(x, next_c)

        return next_c


    def _handle_grammar(self, next_obj, children) -> List[GrammarNode]:
        if isinstance(next_obj, UnitType):
            return [GrammarNode(next_obj.name, children)]

        elif isinstance(next_obj, PV):
            return self._handle_grammar(full_grammar[next_obj], children)

        elif isinstance(next_obj, GOr):
            return [self._handle_grammar(x, children)[0] for x in next_obj.args]

        elif isinstance(next_obj, GAnd):
            next_set = self._handle_grammar(next_obj.b, children)
            next_set.extend(children)
            return self._handle_grammar(next_obj.a, next_set)

        else:
            raise ValueError('Something went wrong...')

