from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.sym_event import SymEvent, VariableEvent
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
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

        result.nl_event = contract.try_get_event(ob_val, 'obligations', 'consequent')

        return result
    

    # def _get_nl_event(self, contract: SymboleoContract, ob_var: str):
    #     sym_evt: VariableEvent = contract.try_get_event(ob_var, 'obligations', 'consequent')

    #     if sym_evt:
    #         event = self._get_event(contract, sym_evt.name)
    #         event.is_new = False
    #         return event
    #     else:
    #         raise Exception(f'Invalid obligation reference... {ob_var}')
    

    # def _get_event(self, contract: SymboleoContract, evt_name:str) -> CustomEvent:
    #     decl = contract.contract_spec.declarations[evt_name]
    #     if decl.base_type == 'events':
    #         return decl.evt
    #     return None