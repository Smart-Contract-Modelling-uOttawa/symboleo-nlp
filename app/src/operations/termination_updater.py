from app.classes.symboleo_contract import SymboleoContract

from app.classes.spec.contract_spec import Power
from app.classes.spec.p_atoms import PAtomPredicateTrueLiteral
from app.classes.spec.power_function import PowerFunction, PFContract, PFContractName

from app.src.grammar.selection import Selection
from app.src.operations.parameter_refiner import ParameterRefiner, ParameterConfig, ParameterOperation


class TerminationOperation:
    def __init__(
        self,
        norm_id: str,
        debtor: str,
        creditor: str,
        selection: Selection
        ):
        self.norm_id = norm_id
        self.debtor = debtor 
        self.creditor = creditor
        self.selection = selection
        
class IAddPower:
    def update(self, contract: SymboleoContract, operation: TerminationOperation):
        raise NotImplementedError()
    

class TerminationUpdater(IAddPower):
    def __init__(
        self,
        parm_refiner: ParameterRefiner
    ):
        self.__parm_refiner = parm_refiner


    def update(self, contract: SymboleoContract, operation: TerminationOperation) -> SymboleoContract:
        # Add the blank termination power
        new_power = Power(operation.norm_id, None, operation.debtor, operation.creditor, PAtomPredicateTrueLiteral(), PFContract(PFContractName.Terminated))
        contract.add_norm(new_power)

        # Add the condition
        parm_config = ParameterConfig('powers', operation.norm_id, 'trigger')
        parm_op = ParameterOperation(parm_config, operation.selection)
        self.__parm_refiner.refine(contract, parm_op)
