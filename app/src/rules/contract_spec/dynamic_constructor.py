import inspect
import copy
from typing import List
from app.classes.graph.digraph import Digraph
from app.classes.processing.scored_components import ScoredType, ScoredComponent

# May rename to RecursiveConstructor
class IConstructDynamicObjects:
    # Attempt to construct the target class from the set of args
    # TODO: Return a scored predicate (full predicate, not a type)
    def construct(self, scored_type: ScoredType, scored_parts: List[ScoredComponent]) -> ScoredComponent:
        raise NotImplementedError()

# Shouldn't JUST be for predicates. needs to be more dynamic...
# Case 1: The target is a Predicate (e.g. Happens) and the parms are primitives (TBD)
# Case 2: The target is a primitive (TBD) and the parms are leaves
# Probably just make it all be ScoredObject
# Or at least distinguish between a Type and an Object?
class DynamicObjectConstructor(IConstructDynamicObjects):
    def __init__(self, graph: Digraph):
        self.__graph = graph
    
    def construct(self, scored_type: ScoredType, scored_parts: List[ScoredComponent]) -> ScoredComponent:
        #n_arg_set = [copy.deepcopy(x) for x in possible_parms]
        score = scored_type.score
        target_class = scored_type.obj_type
        target_parms = inspect.signature(target_class.__init__).parameters
        final_args = {}

        # Need a way to handle str - should probably skip over those as well?
        for tp_key in target_parms:
            if tp_key == 'self': 
                continue
            
            target_type = target_parms[tp_key].annotation
            for sp in scored_parts: # should copy the parms and remove as I find them...
                if self.__graph.is_subclass(type(sp.obj).__name__, target_type.__name__):
                    final_args[tp_key] = sp.obj
                    score += sp.score # TODO: Use a better function than simple addition
                    # Remove it from the list?
                    continue # This means we're choosing the first one... May not be ideal?
            
            
        # TODO: Wrap in try-catch?
        if len(target_parms) == len(final_args) + 1:
            target_obj = target_class(**final_args)
            score = min(score, 1)
            return ScoredComponent(target_obj, score)
        else:
            return None


# Major issue with this approach:
## Graph-like nature of the classes means that something like ObligationEvent is a subclass of a SymPoint
## This creates ambiguities
## Potential solution: Enforce a more tree-like structure. No shared primitives for events/points/etc

