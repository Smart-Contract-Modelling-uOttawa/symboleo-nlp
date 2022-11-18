from app.classes.symboleo_contract import SymboleoContract
from app.src.processor_lookup import ILookupProcessor
from app.classes.contract_update_request import ContractUpdateRequest

class IUpdateContracts:
    def update(self, req: ContractUpdateRequest) -> SymboleoContract:
        raise NotImplementedError()


class ContractUpdater(IUpdateContracts):
    def __init__(
        self,
        processor_lookup: ILookupProcessor
    ):
        self.__lookup = processor_lookup
    

    def update(self, req: ContractUpdateRequest) -> SymboleoContract:
        processor = self.__lookup.lookup(req.key)
        result = processor.process(req)
        return result
