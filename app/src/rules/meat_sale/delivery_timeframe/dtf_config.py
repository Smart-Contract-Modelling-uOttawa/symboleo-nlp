from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensAfter, PredicateFunctionWHappensBefore, PredicateFunctionWHappensBeforeEvent
from app.classes.spec.sym_point import PointAtomParameterDotExpression, PointFunction, PointAtomContractEvent
from app.classes.spec.sym_event import ContractEvent, VariableEvent
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt, VariableDotExpression
from app.src.rules.shared.configs import PredicateExtractorConfig
from app.src.rules.shared.case_obj import CaseObj
from app.src.rules.meat_sale.delivery_timeframe.dtf_matcher import get_dtf_matcher

def get_dtf_pred_config(nlp) -> PredicateExtractorConfig:
    # The template should come from the deltas file. Store the obj, not the string
    delivered = {
        'name': 'delivered'
    }
    delivered_vde = VariableDotExpression(delivered['name'])
    delivered_event = VariableEvent(delivered_vde)
    template = PredicateFunctionHappens(delivered_event)

    matcher = get_dtf_matcher(nlp)
    
    case_dict = {
        'within_time_period': CaseObj([PointFunction], PredicateFunctionWHappensBefore),
        'before_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionWHappensBefore),
        'after_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionHappensAfter),
        'before_event': CaseObj([VariableEvent], PredicateFunctionWHappensBeforeEvent),
        'after_event': CaseObj([None], None),
        'between_date_and_date': CaseObj([None], None),
        'within_time_period_of_event': CaseObj([None], None)
    }

    # Can maybe just do this for all primitives... just loop through them
    primitive_dict = {
        'time_value_int': TimeValueInt,
        'time_unit_string': TimeUnitStr,
        'point_vde': VariableDotExpression,
        'event_vde': VariableDotExpression
    }

    contract_event = ContractEvent('activated')
    default_components = [
        PointAtomContractEvent(contract_event)
    ]

    return PredicateExtractorConfig(template, matcher, case_dict, primitive_dict, default_components)
