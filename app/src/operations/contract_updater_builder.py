from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.parm_operations.parameter_updater_builder import ParameterUpdaterBuilder


class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        parm_updater = ParameterUpdaterBuilder.build()
        tp_adder = None
        do_adder = None

        result = ContractUpdater(parm_updater, tp_adder, do_adder)
        return result