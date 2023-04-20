from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract

from app.classes.spec.norm import Power
from app.classes.spec.p_atoms import PAtomPredicateTrueLiteral
from app.classes.spec.power_function import PowerFunction, PFContract, PFContractName
from app.classes.selection.selected_node import SelectedNode

from app.src.operations.refine_parameter2.parameter_refiner import ParameterRefiner, ParameterOperation


class TerminationOperation:
    def __init__(
        self,
        norm_id: str,
        debtor: str,
        creditor: str,
        node_list: List[SelectedNode],
        ):
        self.norm_id = norm_id
        self.debtor = debtor 
        self.creditor = creditor
        self.node_list = node_list
        
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
        power_string = f'{operation.debtor} may terminate the contract.'
        contract.add_norm(new_power, operation.norm_id, power_string)

        # Add the condition
        parm_op = ParameterOperation(operation.norm_id, operation.node_list)
        self.__parm_refiner.refine(contract, parm_op)