from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.contract_updater import IUpdateContractOp

from app.classes.spec.contract_spec import Power
from app.classes.spec.p_atoms import PAtomPredicateTrueLiteral
from app.classes.spec.power_function import PowerFunction, PFContract, PFContractName

from app.src.operations.parm_operations.parameter_updater import ParameterOperation, IUpdateParameter


class TerminationOperation:
    def __init__(
        self,
        norm_id: str,
        debtor: str,
        creditor: str,
        parm_operation: ParameterOperation
        ):
        self.norm_id = norm_id
        self.debtor = debtor 
        self.creditor = creditor
        self.parm_operation = parm_operation
        

class TerminationUpdater(IUpdateContractOp):
    def __init__(
        self,
        norm_adder: IUpdateParameter,
        parameter_updater: IUpdateContractOp
    ):
        self.__norm_adder = norm_adder
        self.__parameter_updater = parameter_updater


    def update(self, contract: SymboleoContract, operation: TerminationOperation) -> SymboleoContract:
        # Add the blank termination power
        new_power = Power(operation.norm_id, None, operation.debtor, operation.creditor, PAtomPredicateTrueLiteral(), PFContract(PFContractName.Terminated))
        contract = self.__norm_adder.update(contract, None, new_power)

        # Add the condition
        contract = self.__parameter_updater.update(contract, operation.parm_operation)
        
        return contract