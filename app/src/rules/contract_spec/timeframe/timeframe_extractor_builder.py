from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensAfter, PredicateFunctionWHappensBefore, PredicateFunctionWHappensBeforeEvent
from app.classes.spec.sym_point import PointAtomParameterDotExpression, PointFunction, PointAtomContractEvent, PointVDE
from app.classes.spec.sym_event import ContractEvent, VariableEvent, EventVDE
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt
from app.src.rules.shared.configs import PredicateExtractorConfig
from app.src.rules.shared.case_obj import CaseObj
from app.src.rules.contract_spec.timeframe.timeframe_matcher import get_tf_matcher
from app.classes.spec.predicate_function import PredicateFunction

from app.src.rules.shared.interfaces import IBuildPredicateExtractor, IExtractPredicates
from app.src.rules.contract_spec.predicate_extractor import PredicateExtractor
from app.src.rules.contract_spec.dynamic_constructor_builder import DynamicConstructorBuilder
from app.src.primitive_identifiers.primitive_scorer import PrimitiveScorer

class TimeFrameExtractorBuilder(IBuildPredicateExtractor):
    @staticmethod
    def build(
        nlp, 
        template: PredicateFunction,
        default_components = []
    ) -> IExtractPredicates:
        matcher = get_tf_matcher(nlp)
        
        case_dict = {
            'within_time_period': CaseObj([PointFunction], PredicateFunctionWHappensBefore),
            'before_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionWHappensBefore),
            'after_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionHappensAfter),
            'before_event': CaseObj([VariableEvent], PredicateFunctionWHappensBeforeEvent),
            'after_event': CaseObj([None], None),
            'between_date_and_date': CaseObj([None], None),
            'within_time_period_of_event': CaseObj([None], None),
            'until_adp_event': CaseObj([PointFunction], PredicateFunctionWHappensBefore)
        }

        target_primitives = [TimeValueInt, TimeUnitStr, PointVDE, EventVDE]

        # TODO: The PointAtomContractEvent is not a primitive - may want to address this...
        # Perhaps I just send along the ContractEvent instead
        contract_event = ContractEvent('activated')
        default_components = [
            PointAtomContractEvent(contract_event)
        ]

        config = PredicateExtractorConfig(template, matcher, case_dict, target_primitives, default_components)
        
        dynamic_constructor = DynamicConstructorBuilder.build()
        
        primitive_scorer = PrimitiveScorer(nlp)

        return PredicateExtractor(nlp, config, primitive_scorer, dynamic_constructor)
