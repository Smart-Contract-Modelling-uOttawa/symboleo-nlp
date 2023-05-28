from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import ContractEventName, ContractEvent
from app.classes.elements.standard_event_elements import ContractSubjectNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

class ContractSubjectNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: ContractSubjectNode,  value: any) -> UpdatePackage:
            if isinstance(value, ContractEventName):
                new_value = ContractEvent(value)
                return UpdatePackage(new_value=new_value)

