from typing import List, Dict
from app.classes.spec.primitive import Primitive
from app.classes.spec.primitive import ScoredPrimitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives
from app.src.matcher_helper import MyMatcher

# Import all identifiers
from app.src.primitive_identifiers.time_value_int_identifier import TimeValueIntIdentifier
from app.src.primitive_identifiers.time_unit_str_identifier import TimeUnitStrIdentifier
from app.src.primitive_identifiers.point_vde_identifier import PointVdeIdentifier
from app.src.primitive_identifiers.event_vde_identifier import EventVdeIdentifier
from app.src.primitive_identifiers.obligation_event_identifier import ObligationEventIdentifier
from app.src.primitive_identifiers.point_function_identifier import PointFunctionIdentifier

# Import all the scorers
from app.classes.spec.sym_event import *
from app.classes.spec.sym_point import *
from app.classes.spec.sym_situation import * 
from app.classes.spec.helpers import *

# Primitive = VariableDotExpression or \
#     ObligationEvent or \
#     ContractEvent or \
#     PowerEvent or \
#     TimeValueInt or \
#     TimeUnit or \
#     ObligationState or \
#     PowerState or \
#     ContractState

# Will NOT be just primitives I dont think. Will be more dynamic
class IScorePrimitives:
    def score(self, target_primitives: List[Primitive], doc) -> List[ScoredPrimitive]:
        raise NotImplementedError()


class PrimitiveScorer(IScorePrimitives):
    def __init__(self, nlp):
        
        my_matcher = MyMatcher(nlp)

        self.__master_dict: Dict[Primitive, IIdentifyPrimitives] = {
            TimeValueInt: TimeValueIntIdentifier(my_matcher),
            TimeUnitStr: TimeUnitStrIdentifier(my_matcher),
            PointVDE: PointVdeIdentifier(my_matcher),
            EventVDE: EventVdeIdentifier(my_matcher),
            ObligationEvent: ObligationEventIdentifier(my_matcher),
            #ObligationState: ObligationStateIdentifier(my_matcher)
            PointFunction: PointFunctionIdentifier(my_matcher)
        }
    
    def score(self, target_primitives: List[Primitive], doc) -> List[ScoredPrimitive]:
        results = []
        
        for x in target_primitives:
            next_result = self.__master_dict[x].identify(doc)
            if next_result:
                results.append(next_result)
        
        return results
    