from app.src.operations.dependency_builder import DependencyBuilder
from app.src.grammar_builder.child_getter import ChildGetter
from app.src.grammar_builder.unit_builders.unit_builder_dict import UnitBuilderDictConstructor 

from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.grammar_builder.grammar_builder_constructor import GrammarBuilderConstructor

from app.web_lib.cache.contract_storage import ContractStorage
from app.web_lib.cache.input_storage import InputStorage
from app.web_lib.cache.grammar_storage import GrammarStorage
from app.web_lib.contract_fetcher import ContractFetcher
from app.web_lib.parameter_selector import ParameterSelector
from app.web_lib.value_processor import ValueProcessor
from app.web_lib.refinement_submitter import RefinementSubmitter
from app.web_lib.grammar_handler import GrammarHandler

class WebDependencies:
    def __init__(
        self,
        contract_fetcher: ContractFetcher,
        parameter_selector: ParameterSelector,
        value_processor: ValueProcessor,
        refinement_submitter: RefinementSubmitter,
        grammar_handler: GrammarHandler
    ):
        self.contract_fetcher = contract_fetcher
        self.parameter_selector = parameter_selector
        self.value_processor = value_processor
        self.refinement_submitter = refinement_submitter
        self.grammar_handler = grammar_handler

class WebDependencyBuilder:
    @staticmethod
    def build(fake:bool = True):
        core_deps = DependencyBuilder.build(fake)

        contract_storage = ContractStorage()
        input_storage = InputStorage()

        pattern_class_getter = AllPatternClassGetter()
        grammar_builder = GrammarBuilderConstructor.construct()
        grammar_storage = GrammarStorage()
        
        child_builder_dict = UnitBuilderDictConstructor.build()
        child_getter = ChildGetter(child_builder_dict)

        grammar_handler = GrammarHandler(
            pattern_class_getter,
            grammar_builder,
            grammar_storage,
            child_getter
        )

        contract_fetcher = ContractFetcher(contract_storage)
        parameter_selector = ParameterSelector(contract_storage, input_storage, grammar_handler)
        value_processor = ValueProcessor(contract_storage, input_storage, grammar_handler)

        contract_updater = ContractUpdaterBuilder.build(core_deps)
        refinement_submitter = RefinementSubmitter(contract_storage, input_storage, contract_updater)

        return WebDependencies(
            contract_fetcher,
            parameter_selector,
            value_processor,
            refinement_submitter,
            grammar_handler
        )

