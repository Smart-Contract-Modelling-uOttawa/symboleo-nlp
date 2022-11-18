from typing import List, Tuple
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.meat_sale.delivery_location.address_extractor import IExtractAddresses

class AddressScorer(IScoreStuff):
    def __init__(
        self, 
        nlp,
        address_extractor: IExtractAddresses
    ):
        self.__nlp = nlp
        self.__address_extractor = address_extractor
    
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        addresses = self.__address_extractor.extract(req.doc)
        return [(ad, 0.2) for ad in addresses] 
