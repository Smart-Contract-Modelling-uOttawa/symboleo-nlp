from copy import deepcopy
from app.classes.symboleo_contract import ContractSpec, DomainModel, SymboleoContract
from app.src.atom_extractor import IExtractAtoms

class ContractUpdateRequest:
    new_sentence: str = ''
    key: str = ''
    contract: SymboleoContract = None # Need a type here
    

class IUpdateContracts:
    def update(self, req: ContractUpdateRequest) -> SymboleoContract:
        raise NotImplementedError()


class ContractUpdater(IUpdateContracts):
    def __init__(
        self,
        atom_extractor: IExtractAtoms
    ):
        self.__atom_extractor = atom_extractor
    
    def update(self, req: ContractUpdateRequest) -> SymboleoContract:
        # do stuff here
        new_domain_model: DomainModel = deepcopy(req.contract.domain_model)
        new_contract_spec: ContractSpec = deepcopy(req.contract.contract_spec)

        # Perform some validation based on the new_sentence and the key
        ## This may also do some basic extraction? since we will be running it through the NLP pipeline

        # Identify the most likely primitives -> list of primitives + scores
        ## Will also involve processing the domain model


        # Orchestrate the primitives to get the possible candidates

        return SymboleoContract(new_domain_model, new_contract_spec)
