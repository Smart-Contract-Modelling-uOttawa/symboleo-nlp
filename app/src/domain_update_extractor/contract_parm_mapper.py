from typing import List
from app.classes.helpers.parm_checker import ParmChecker
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass

class IMapContractParms:
    def map(self, pattern_class: PatternClass) -> List[ContractSpecParameter]:
        raise NotImplementedError()


class ContractParmMapper(IMapContractParms):
    def map(self, pattern_class: PatternClass) -> List[ContractSpecParameter]:
        results = []

        if isinstance(pattern_class, EventPatternClass):
            evt = pattern_class.nl_event
            if evt.dobj and evt.dobj.is_parm:
                parm_name = self._convert_parm_name(evt.dobj.head)
                new_parm = ContractSpecParameter(parm_name, evt.dobj.asset_type)
                results.append(new_parm)
            
        
        if PV.DATE in pattern_class.val_dict:
            date_text = pattern_class.val_dict[PV.DATE]
            if ParmChecker.is_parm(date_text):
                parm_name = self._convert_parm_name(pattern_class.val_dict[PV.DATE])
                new_parm = ContractSpecParameter(parm_name, 'Date')
                results.append(new_parm)


        return results


    def _convert_parm_name(self, s:str) -> str:
        return s[1:-1].lower()