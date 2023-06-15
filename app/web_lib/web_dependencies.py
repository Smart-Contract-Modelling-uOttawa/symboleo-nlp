from app.src.operations.dependency_builder import DependencyBuilder
from app.src.selection.child_node_getter import IGetNodeChildren, ChildNodeGetter
from app.src.selection.child_getters.child_getter_dict import ChildGetterDictConstructor 

from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

from app.web_lib.contract_storage import ContractStorage
from app.web_lib.input_storage import InputStorage
from app.web_lib.contract_fetcher import ContractFetcher
from app.web_lib.parameter_selector import ParameterSelector
from app.web_lib.value_processor import ValueProcessor
from app.web_lib.refinement_submitter import RefinementSubmitter

class WebDependencies:
    def __init__(
        self,
        contract_fetcher: ContractFetcher,
        parameter_selector: ParameterSelector,
        value_processor: ValueProcessor,
        refinement_submitter: RefinementSubmitter
    ):
        self.contract_fetcher = contract_fetcher
        self.parameter_selector = parameter_selector
        self.value_processor = value_processor
        self.refinement_submitter = refinement_submitter

class WebDependencyBuilder:
    @staticmethod
    def build(fake:bool = True):
        core_deps = DependencyBuilder.build(fake)

        contract_storage = ContractStorage()
        input_storage = InputStorage()

        child_getter_dict = ChildGetterDictConstructor.build()
        child_node_getter = ChildNodeGetter(child_getter_dict)

        contract_fetcher = ContractFetcher(contract_storage)
        parameter_selector = ParameterSelector(child_node_getter, contract_storage, input_storage)
        value_processor = ValueProcessor(child_node_getter, contract_storage, input_storage)

        contract_updater = ContractUpdaterBuilder.build(core_deps)
        refinement_submitter = RefinementSubmitter(contract_storage, input_storage, contract_updater)

        return WebDependencies(
            contract_fetcher,
            parameter_selector,
            value_processor,
            refinement_submitter
        )

