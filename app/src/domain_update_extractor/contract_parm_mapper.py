from typing import List
from app.classes.helpers.parm_checker import ParmChecker
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.norm_config import NormConfig
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.src.object_mappers.date_mapper import IMapDate

class IMapContractParms:
    def map(self, pattern_class: PatternClass, norm_config: NormConfig) -> List[ContractSpecParameter]:
        raise NotImplementedError()


class ContractParmMapper(IMapContractParms):
    def __init__(self, date_mapper: IMapDate):
        self.__date_mapper = date_mapper

    def map(self, pattern_class: PatternClass, norm_config: NormConfig) -> List[ContractSpecParameter]:
        results = []

        if isinstance(pattern_class, EventPatternClass):
            evt = pattern_class.nl_event
            if evt.dobj and evt.dobj.is_parm:
                parm_name = ParmChecker.lower_parm(evt.dobj.head)
                new_parm = ContractSpecParameter(parm_name, evt.dobj.asset_type)
                results.append(new_parm)
            
        
        for pv in [PV.DATE, PV.DATE2]:

            if pv in pattern_class.val_dict:
                date_text = pattern_class.val_dict[pv]
                parm_name = self.__date_mapper.map(date_text, pv, norm_config)
                new_parm = ContractSpecParameter(parm_name, 'Date') # Value is lost
                results.append(new_parm)
        


        return results

