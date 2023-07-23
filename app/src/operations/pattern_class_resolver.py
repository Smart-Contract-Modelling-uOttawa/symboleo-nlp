from typing import List
from app.classes.spec.norm_config import NormConfig
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.spec.p_atoms import PAtomPredicateTrueLiteral, PAtomPredicateFalseLiteral

class IResolvePatternClasses:
    def resolve(self, pattern_classes: List[PatternClass], norm_config: NormConfig) -> PatternClass:
        raise NotImplementedError()
    
class PatternClassResolver(IResolvePatternClasses):
    def resolve(self, pattern_classes: List[PatternClass], norm_config: NormConfig) -> PatternClass:
        if len(pattern_classes) == 1:
            return pattern_classes[0]
        
        pc_types = [type(x) for x in pattern_classes]

        # Will need special resolution rules for different cases
        if type(AfterEvent()) in pc_types and type(CondAEvent()) in pc_types:
            antecedent = norm_config.norm.get_component('antecedent')

            # If the antecedent is the default (T/F) => new conditional
            if isinstance(antecedent, (PAtomPredicateTrueLiteral, PAtomPredicateFalseLiteral)):
                return CondAEvent()
            else:
                # Othewise, the conditional already has something in it -> temporal refinement
                AfterEvent()

        # Other special cases will go here...

        return pattern_classes[0]