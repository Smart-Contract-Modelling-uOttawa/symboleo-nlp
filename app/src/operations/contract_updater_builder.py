from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.refine_parameter.parameter_refiner import ParameterRefiner
from app.src.operations.domain_updater import DomainUpdater
from app.src.operations.add_power.termination_updater import TerminationUpdater

from app.src.operations.refine_parameter.operation_runner import RefinementOperationRunner
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        frame_checker = FrameCheckerConstructor.construct()
        refinement_runner = RefinementOperationRunner()
        parm_refiner = ParameterRefiner(frame_checker, refinement_runner)
        tp_adder = TerminationUpdater(parm_refiner)
        do_adder = DomainUpdater()

        return ContractUpdater(parm_refiner, tp_adder, do_adder)