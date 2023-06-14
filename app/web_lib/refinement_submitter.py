from app.src.operations.parameter_refiner import IRefineParameter

from app.classes.operations.parameter_operation import ParameterOperation
from app.web_lib.contract_obj import WebContract
from app.web_lib.contract_storage import ContractStorage
from app.web_lib.input_storage import InputStorage

class RefinementSubmitter:
    def __init__(
        self,
        contract_storage: ContractStorage,
        input_storage: InputStorage,
        parameter_refiner: IRefineParameter
    ):
        self.__contract_storage = contract_storage
        self.__input_storage = input_storage
        self.__parameter_refiner = parameter_refiner


    def submit(self, contract_id: str, nl_key: str, parm_key: str, unique_key:str):
        elements = self.__input_storage.get_final(unique_key)

        op = ParameterOperation(
            nl_key,
            parm_key,
            elements
        )

        contract = self.__contract_storage.load(unique_key, contract_id)

        self.__parameter_refiner.refine(contract, op)
        
        # Will likely want to do something with the parameters as well
        # May clear the elements cache as well
        self.__contract_storage.store(unique_key, contract_id, contract)

        return WebContract(contract)


