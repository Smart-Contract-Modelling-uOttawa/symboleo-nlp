from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.dependency_builder import DependencyBuilder

from app.src.operations.operation_mapper_builder import OperationMapperBuilder
from app.src.nl_creator.nl_creator_builder import NLCreatorBuilder

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        deps = DependencyBuilder.build(fake=True)
        operation_mapper = OperationMapperBuilder.build(deps)
        nl_creator = NLCreatorBuilder()
        return ContractUpdater(operation_mapper, nl_creator)