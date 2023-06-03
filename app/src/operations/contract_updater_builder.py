from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.domain_updater import DomainUpdater
from app.src.operations.termination_updater import TerminationUpdater
from app.src.selection.element_extractor_builder import ElementExtractorBuilder
from app.src.operations.parameter_refiner_constructor import ParameterRefinerConstructor
from app.src.operations.dependency_builder import DependencyBuilder
from app.src.operations.user_input_cleaner import UserInputCleaner

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        deps = DependencyBuilder.build(fake=True)
        input_cleaner = UserInputCleaner()
        element_extractor = ElementExtractorBuilder.build(deps)
        parm_refiner = ParameterRefinerConstructor.construct(deps)
        tp_adder = TerminationUpdater(parm_refiner)
        do_adder = DomainUpdater()

        return ContractUpdater(input_cleaner, element_extractor, parm_refiner, tp_adder, do_adder)