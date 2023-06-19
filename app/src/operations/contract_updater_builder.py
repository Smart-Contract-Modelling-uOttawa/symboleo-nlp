from app.classes.operations.dependencies import Dependencies

from app.src.operations.contract_updater import ContractUpdater

from app.src.operations.operation_mapper_builder import OperationMapperBuilder

class ContractUpdaterBuilder:
    @staticmethod
    def build(deps: Dependencies) -> ContractUpdater:
        operation_mapper = OperationMapperBuilder.build(deps)
        return ContractUpdater(operation_mapper)