from typing import List, Type, Dict
from app.classes.grammar.g_and import GAnd
from app.classes.grammar.g_or import GOr

from app.classes.grammar.grammar_node import GrammarNode
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.grammar.full_grammar import UnitType, GrammarUnit

# Make a function here...
from app.classes.pattern_classes.all_pattern_classes import *

class IBuildPatternTrees:
    def build(self, pattern_class: Type[PatternClass]) -> List[GrammarNode]:
        raise NotImplementedError()


class PatternTreeBuilder(IBuildPatternTrees):
    def __init__(self, grammar: Dict[PV, GrammarUnit]):
        self.__grammar = grammar
    
    def build(self, pattern_class: Type[PatternClass]) -> List[GrammarNode]:
        next_c: List[GrammarNode] = []
        
        for x in reversed(pattern_class.sequence):
            next_c = self._handle_grammar(x, next_c)

        return next_c


    def _handle_grammar(self, next_obj, children) -> List[GrammarNode]:
        if isinstance(next_obj, UnitType):
            return [GrammarNode(next_obj.name, children)]

        elif isinstance(next_obj, PV):
            return self._handle_grammar(self.__grammar[next_obj], children)

        elif isinstance(next_obj, GOr):
            return [self._handle_grammar(x, children)[0] for x in next_obj.args]

        # GAnd
        else:
            next_obj: GAnd = next_obj
            next_set = self._handle_grammar(next_obj.b, children)
            #next_set.extend(children)
            return self._handle_grammar(next_obj.a, next_set)
