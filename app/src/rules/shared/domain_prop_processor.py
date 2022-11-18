import copy
from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.symboleo_contract import SymboleoContract
from app.classes.domain_model.domain_model import DomainProp
from app.src.rules.shared.configs import DomainPropProcessorConfig
from app.src.rules.shared.interfaces import IProcessDocs, IExtractProperties

# Processes and updates a domain prop
class DomainPropProcessor(IProcessDocs):
    def __init__(
        self,
        config: DomainPropProcessorConfig,
        prop_extractor: IExtractProperties
    ):
        self.__config = config
        self.__prop_extractor = prop_extractor


    def process(self, req: ContractUpdateRequest) -> SymboleoContract:
        new_dm = copy.deepcopy(req.contract.domain_model)
    
        target_event = new_dm.__dict__[self.__config.obj_type][self.__config.obj_name]

        prop_value = self.__prop_extractor.extract(req)

        new_prop = DomainProp(self.__config.new_prop_name, prop_value, self.__config.new_prop_type)
        target_event.props.append(new_prop)

        return SymboleoContract(new_dm, req.contract.contract_spec, req.contract.template_strings)
