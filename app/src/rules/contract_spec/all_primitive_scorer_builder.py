from typing import Dict, Type
from app.src.matcher_helper import MyMatcher

from app.classes.processing.components import Primitive
from app.classes.processing.components import *

# Import all identifiers
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.component_identifiers.time_value_int_scorer import TimeValueIntScorer
from app.src.component_identifiers.time_unit_str_scorer import TimeUnitStrScorer
from app.src.component_identifiers.point_vde_scorer import PointVdeScorer
from app.src.component_identifiers.point_function_scorer import PointFunctionScorer
from app.src.component_identifiers.contract_event_scorer import ContractEventScorer
#from app.src.primitive_identifiers.event_vde_identifier import EventVdeIdentifier
from app.src.component_identifiers.obligation_event_scorer import ObligationEventScorer

from app.src.rules.contract_spec.all_primitives_scorer import AllPrimitivesScorer

# Need to decide which are the key primitives... 
# Will depend on structure of the symboleo graph

class AllPrimitiveScorerBuilder:
    @staticmethod
    def build(nlp) -> Dict[str, IScorePrimitives]:

        my_matcher = MyMatcher(nlp)

        # PointFunction
        tvi_scorer = TimeValueIntScorer(my_matcher)
        tus_scorer = TimeUnitStrScorer(my_matcher)
        point_function_scorer = PointFunctionScorer(my_matcher, tvi_scorer, tus_scorer)

        # ContractEvent
        contract_event_scorer = ContractEventScorer(None)

        obligation_event_scorer = ObligationEventScorer(my_matcher)

        my_dict: Dict[str, IScorePrimitives] = {
            'PointVDE': PointVdeScorer(my_matcher),
            'PointFunction': point_function_scorer,
            'ContractEvent': contract_event_scorer,
            'ObligationEvent': obligation_event_scorer

            # ...
        }

        return AllPrimitivesScorer(my_dict)
