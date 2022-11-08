from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensAfter, PredicateFunctionWHappensBefore, PredicateFunctionWHappensBeforeEvent
from app.classes.spec.sym_point import PointAtomParameterDotExpression, PointFunction, PointAtomContractEvent
from app.classes.spec.sym_event import ContractEvent, VariableEvent
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt, VariableDotExpression
from app.src.rules.shared.i_config import IConfig
from app.src.rules.shared.case_obj import CaseObj
from app.src.rules.meat_sale.delivery_timeframe.matchers import get_matcher


class DeliveryTimeframeConfig(IConfig):
    template = None
    matcher = None
    case_dict = None
    primitive_dict = None
    default_components = None
    
    def __init__(
        self, 
        nlp
    ):
        # The template should come from the deltas file. Store the obj, not the string
        delivered = {
            'name': 'delivered'
        }
        delivered_vde = VariableDotExpression(delivered['name'])
        delivered_event = VariableEvent(delivered_vde)
        self.template = PredicateFunctionHappens(delivered_event)

        self.matcher = get_matcher(nlp)
        
        self.case_dict = {
            'within_time_period': CaseObj([PointFunction], PredicateFunctionWHappensBefore),
            'before_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionWHappensBefore),
            'after_date': CaseObj([PointAtomParameterDotExpression], PredicateFunctionHappensAfter),
            'before_event': CaseObj([VariableEvent], PredicateFunctionWHappensBeforeEvent),
            'after_event': CaseObj([None], None),
            'between_date_and_date': CaseObj([None], None),
            'within_time_period_of_event': CaseObj([None], None)
        }

        # Can maybe just do this for all primitives... just loop through them
        self.primitive_dict = {
            'time_value_int': TimeValueInt,
            'time_unit_string': TimeUnitStr,
            'point_vde': VariableDotExpression,
            'event_vde': VariableDotExpression
        }

        contract_event = ContractEvent('activated')
        self.default_components = [
            PointAtomContractEvent(contract_event)
        ]
