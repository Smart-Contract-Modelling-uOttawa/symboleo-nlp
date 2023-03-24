from app.src.operations.termination_operations.termination_updater import TerminationUpdater

from app.src.operations.parm_operations.parameter_updater_builder import ParameterUpdaterBuilder
from app.src.operations.parm_operations.norm_adder import NormAdder

from app.src.operations.domain_operations.dm_object_adder import DomainObjectAdder
from app.src.operations.domain_operations.declaration_adder import DeclarationAdder

class TerminationUpdaterBuilder: # pragma: no cover
    @staticmethod
    def build() -> TerminationUpdater:
        norm_adder = NormAdder()
        parm_updater = ParameterUpdaterBuilder.build()
        return TerminationUpdater(norm_adder, parm_updater)