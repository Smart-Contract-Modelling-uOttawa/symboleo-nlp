from app.templates.template_getter import get_template

from app.web_lib.contract_obj import WebContract

from app.web_lib.contract_storage import ContractStorage

# May enforce
allowed_ids = [
    'meat_sale',
    'indep',
    'biomass',
    'rental',
    'prop',
    'sample'
]

class ContractFetcher:
    def __init__(
        self, 
        contract_storage: ContractStorage
    ):
        self.__contract_storage = contract_storage

    def fetch(self, contract_id: str, unique_key:str) -> WebContract:
        contract =  get_template(contract_id)

        self.__contract_storage.store(unique_key, contract_id, contract)

        result = WebContract(contract)
        return result

