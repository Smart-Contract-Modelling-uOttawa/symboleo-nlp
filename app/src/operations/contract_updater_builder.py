from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.domain_updater import DomainUpdater
from app.src.operations.add_power.termination_updater import TerminationUpdater
from app.src.operations.refine_parameter2.parameter_refiner_constructor import ParameterRefinerConstructor

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        parm_refiner = ParameterRefinerConstructor.construct()
        tp_adder = TerminationUpdater(parm_refiner)
        do_adder = DomainUpdater()

        return ContractUpdater(parm_refiner, tp_adder, do_adder)