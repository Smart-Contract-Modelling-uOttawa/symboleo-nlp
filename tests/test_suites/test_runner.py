from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder
from app.src.operations.contract_updater_config import UpdateConfig

class TestRunner:
    def __init__(self):
        self.__contract_updater = ContractUpdaterBuilder.build()
    
    def update_contract(self, contract: SymboleoContract, config: UpdateConfig):
        self.__contract_updater.update(contract, config.op_code, config)


    
