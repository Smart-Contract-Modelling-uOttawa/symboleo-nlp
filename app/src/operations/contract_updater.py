from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.spec.contract_spec import Norm
from app.classes.spec.domain_model import DomainProp 

from app.src.operations.configs import OpCode, ParameterConfig
from app.src.operations.predicate_refiner import IRefinePredicates
from app.src.operations.trigger_adder import IAddTriggers
from app.src.operations.dm_prop_adder import IAddDomainProps
from app.src.operations.norm_adder import IAddNorms

UpdateObjType = PredicateFunction or Norm or DomainProp

# A flexible orchestrator for all types of parameter-based contract updates
## Might rename this to reflect that this is for parameter-based norm updates
class ContractUpdater:
    def __init__(
            self,
            predicate_refiner: IRefinePredicates,
            trigger_adder: IAddTriggers,
            norm_adder: IAddNorms,
            dm_prop_adder: IAddDomainProps
        ):
        self.__predicate_refiner = predicate_refiner
        self.__trigger_adder = trigger_adder
        self.__norm_adder = norm_adder
        self.__dm_prop_adder = dm_prop_adder

    def update(
            self, 
            op_code: OpCode,
            contract: SymboleoContract, 
            update_obj: UpdateObjType,
            config: ParameterConfig = None, 
        ) -> SymboleoContract:
            if op_code == OpCode.REFINE_PREDICATE:
                return self.__predicate_refiner.refine(config, contract, update_obj)
            
            elif op_code == OpCode.ADD_TRIGGER:
                return self.__trigger_adder.add(config, contract, update_obj)
            
            elif op_code == OpCode.ADD_DM_PROP:
                return self.__dm_prop_adder.add(config, contract, update_obj)
            
            elif op_code == OpCode.ADD_NORM:
                return self.__norm_adder.add(contract, update_obj)

            else:
                raise NotImplementedError('Unknown operation')

