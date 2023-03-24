from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.parm_operations.parameter_updater_builder import ParameterUpdaterBuilder
from app.src.operations.domain_operations.domain_updater_builder import DomainUpdaterBuilder
from app.src.operations.termination_operations.termination_updater_builder import TerminationUpdaterBuilder

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        parm_updater = ParameterUpdaterBuilder.build()
        tp_adder = TerminationUpdaterBuilder.build()
        do_adder = DomainUpdaterBuilder.build()

        result = ContractUpdater(parm_updater, tp_adder, do_adder)
        return result