from typing import List, Dict
import copy
from app.classes.patterns.pattern_classes import *
from app.classes.units.unit_type import UnitType
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.spec.sym_event import VariableEvent, SymEvent, ObligationEvent, ObligationEventName
from app.classes.spec.declaration import EventDeclaration
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UserInput

from app.src.nl_creator.nl_fillers.nl_unit_filler import IFillNLUnit

class ObligationSubjectFiller(IFillNLUnit):
    def fill(self, contract: SymboleoContract, curr: List[str], input_list: List[UserInput], i: int) -> List[str]:
        result = copy.deepcopy(curr)

        val = input_list[i].value 

        ob_var = val.split('.')[1]

        ob_event = self._get_ob_event(input_list, i)

        evt_name = self._get_event_name(contract, ob_var)
        if evt_name:
            event = self._get_event(contract, evt_name)

            if ob_event and ob_event == ObligationEventName.Violated:
                event.negation = True
        else:
            raise Exception(f'Invalid obligation reference... {ob_var}')
        
        result.append(event.to_text())
        
        return result
    
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

    def _get_ob_event(self, input_list: List[UserInput], i:int) -> ObligationEventName:
        next_input = input_list[i+1]
        if next_input.unit_type == UnitType.OBLIGATION_ACTION:
            return ObligationEventName[next_input.value.capitalize()]
        
        return None


