from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.refine_parameter.parameter_refiner import ParameterRefiner
from app.src.operations.domain_updater import DomainUpdater
from app.src.operations.termination_updater import TerminationUpdater

from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        frame_checker = FrameCheckerConstructor.construct()
        parm_refiner = ParameterRefiner(frame_checker)
        tp_adder = TerminationUpdater(parm_refiner)
        do_adder = DomainUpdater()

        return ContractUpdater(parm_refiner, tp_adder, do_adder)