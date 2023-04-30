from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.domain_updater import DomainUpdater
from app.src.operations.termination_updater import TerminationUpdater
from app.src.operations.refine_parameter.parameter_refiner_constructor import ParameterRefinerConstructor
from app.src.grammar.input_converter_builder import InputConverterBuilder
from app.src.operations.dependency_builder import DependencyBuilder

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        deps = DependencyBuilder.build(fake=True)
        input_converter = InputConverterBuilder.build(deps)
        parm_refiner = ParameterRefinerConstructor.construct(deps)
        tp_adder = TerminationUpdater(parm_refiner)
        do_adder = DomainUpdater()

        return ContractUpdater(input_converter, parm_refiner, tp_adder, do_adder)