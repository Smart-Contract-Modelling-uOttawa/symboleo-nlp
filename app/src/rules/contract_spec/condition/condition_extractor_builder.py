from app.classes.spec.predicate_function import PredicateFunction, PredicateFunctionHappens, PredicateFunctionHappensWithin, PredicateFunctionOccurs
from app.classes.spec.sym_event import ObligationEvent, VariableEvent
from app.classes.spec.sym_interval import Interval, IntervalFunctionEnding
from app.classes.spec.sym_situation import ObligationState
from app.classes.spec.sym_point import PointVDE, PointFunction
from app.classes.spec.helpers import TimeValueInt, TimeUnitStr
from app.src.rules.shared.configs import PredicateExtractorConfig
from app.classes.processing.case_obj import CaseObj
from app.src.rules.shared.interfaces import IBuildPredicateExtractor, IExtractPredicates
from app.src.rules.contract_spec.condition.condition_matcher import get_condition_matcher
from app.src.rules.contract_spec.predicate_extractor import PredicateExtractor
from app.src.rules.contract_spec.dynamic_constructor_builder import DynamicConstructorBuilder
from app.src.component_identifiers.primitive_scorer import PrimitiveScorer



class ConditionExtractorBuilder(IBuildPredicateExtractor):
    @staticmethod
    def build(
        nlp, 
        template: PredicateFunction,
        default_components = []
    ) -> IExtractPredicates:
        matcher = get_condition_matcher(nlp)
        
        case_dict = {
            'if_domain_event': CaseObj([ObligationEvent], PredicateFunctionHappens),
            'until_domain_event': CaseObj([VariableEvent, Interval], PredicateFunctionHappensWithin),
            'unless': CaseObj([ObligationState, IntervalFunctionEnding], PredicateFunctionOccurs)
        }

        target_primitives = [
            ObligationEvent, 
            VariableEvent, 
            PointFunction
            #PointVDE, TimeValueInt, TimeUnitStr
        ]

        config = PredicateExtractorConfig(template, matcher, case_dict, target_primitives, default_components)
        
        dynamic_constructor = DynamicConstructorBuilder.build()
        
        primitive_scorer = PrimitiveScorer(nlp)

        return PredicateExtractor(nlp, config, primitive_scorer, dynamic_constructor)
