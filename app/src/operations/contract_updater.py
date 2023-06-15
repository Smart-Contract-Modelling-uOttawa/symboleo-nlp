from typing import List
import random
import string

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

from app.classes.operations.user_input import UserInput, UnitType
from app.src.operations.operation_mapper import IMapCnlToOperations
from app.src.nl_creator.nl_creator import ICreateNL

class IUpdateContract:
    def update(self, contract: SymboleoContract, op_code: OpCode, config: UpdateConfig):
        raise NotImplementedError()


class ContractUpdater(IUpdateContract):
    def __init__(
        self, 
        operation_mapper: IMapCnlToOperations,
        nl_creator: ICreateNL
    ):
        self.__nl_creator = nl_creator
        self.__operation_mapper = operation_mapper


    def update(self, contract: SymboleoContract, op_code: OpCode, config: UpdateConfig):
        # clean up the input
        user_inputs = self._clean_user_inputs(config.user_inputs)

        # Should add this back to pattern. Each pattern should have a text?
        nl_update = self.__nl_creator.create(user_inputs)

        # Need to get the norm
        norms = contract.get_norms_by_key(config.nl_key, config.parm_key)
        norm = norms[0]

        if op_code == OpCode.UPDATE_PARM:
            update_obj = self.__operation_mapper.map(user_inputs, contract, norm)
            contract.run_updates(update_obj)
            contract.update_nl(config.nl_key, config.parm_key, nl_update)
        
        # elif op_code == OpCode.ADD_TERMINATION_POWER:
        #     term_op = TerminationOperation(config.norm_id, config.debtor, config.creditor, elements)
        #     self.__tp_adder.update(contract, term_op)

        else:
            raise ValueError('Invalid operation requested.')
    

    # TODO: Pull this out...
    def _clean_user_inputs(self, user_inputs: List[UserInput]) -> List[UserInput]:
        results = []
        for x in user_inputs:
            if x.unit_type == UnitType.CUSTOM_EVENT:
                if not x.value:
                    # make it random for now
                    rand_str = self._generate_random_string(8)
                    evt_name = f'evt_{rand_str}'
                    
                    next_unit = UserInput(UnitType.CUSTOM_EVENT, evt_name)
                    results.append(next_unit)
                else:
                    results.append(x)
            else:
                results.append(x)
        return results


    def _generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))