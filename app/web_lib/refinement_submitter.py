from app.src.operations.contract_updater import IUpdateContract

from app.classes.operations.op_code import OpCode
from app.classes.operations.contract_updater_config import UpdateConfig
from app.web_lib.contract_obj import WebContract
from app.web_lib.contract_storage import ContractStorage
from app.web_lib.input_storage import InputStorage

class RefinementSubmitter:
    def __init__(
        self,
        contract_storage: ContractStorage,
        input_storage: InputStorage,
        contract_updater: IUpdateContract
    ):
        self.__contract_storage = contract_storage
        self.__input_storage = input_storage
        self.__contract_updater = contract_updater


    def submit(self, contract_id: str, nl_key: str, parm_key: str, unique_key:str):
        user_inputs = self.__input_storage.get_final(unique_key)

        update_config = UpdateConfig(
            parm_key=parm_key,
            nl_key=nl_key,
            user_inputs=user_inputs
        )

        contract = self.__contract_storage.load(unique_key, contract_id)

        self.__contract_updater.update(contract, OpCode.UPDATE_PARM, update_config)
        
        # Will likely want to do something with the parameters as well
        # May clear the elements cache as well
        self.__contract_storage.store(unique_key, contract_id, contract)

        return WebContract(contract)


