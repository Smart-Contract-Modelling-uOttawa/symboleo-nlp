from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.sym_event import SymEvent, VariableEvent
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName
from app.classes.operations.user_input import UserInput
from app.classes.patterns.pattern_classes import PatternClass, EventPatternClass
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit


class ObligationSubjectFiller(IFillPatternUnit):
    def fill(self, pattern_class: EventPatternClass, contract: SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        val = input_list[i].value

        ob_val = val.split('.')[1] 

        if isinstance(result.event, ObligationEvent):
            result.event.obligation_variable = ob_val
        else:
            result.event = ObligationEvent(ObligationEventName.Activated, ob_val)

        result.nl_event = self._get_nl_event(contract, ob_val)

        return result
    

    def _get_nl_event(self, contract: SymboleoContract, ob_var: str):
        evt_name = self._get_event_name(contract, ob_var)
        if evt_name:
            event = self._get_event(contract, evt_name)
            event.is_new = False
            return event
        else:
            raise Exception(f'Invalid obligation reference... {ob_var}')
    
    
    def _get_event_name(self, contract: SymboleoContract, ob_var: str) -> str:
        ob = contract.contract_spec.obligations[ob_var]
        cons = ob.get_component('consequent')
        if isinstance(cons, PAtomPredicate):
            pred_func = cons.predicate_function
            event: SymEvent = pred_func.event
            if isinstance(event, VariableEvent):
                return event.name
        
        return None


    def _get_event(self, contract: SymboleoContract, evt_name:str) -> CustomEvent:
        decl = contract.contract_spec.declarations[evt_name]
        if decl.base_type == 'events':
            return decl.evt
        return None