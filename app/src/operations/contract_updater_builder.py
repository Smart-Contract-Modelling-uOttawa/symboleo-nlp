from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.domain_updater import DomainUpdater
from app.src.operations.add_power.termination_updater import TerminationUpdater
from app.src.operations.refine_parameter2.parameter_refiner_constructor import ParameterRefinerConstructor
from app.src.operations.input_converter_builder import InputConverterBuilder
from app.src.operations.dependencies import Dependencies
from app.src.operations.dependencies import DependencyBuilder

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        deps = DependencyBuilder.build()
        input_converter = InputConverterBuilder.build(deps)
        parm_refiner = ParameterRefinerConstructor.construct(deps)
        tp_adder = TerminationUpdater(parm_refiner)
        do_adder = DomainUpdater()

        return ContractUpdater(input_converter, parm_refiner, tp_adder, do_adder)