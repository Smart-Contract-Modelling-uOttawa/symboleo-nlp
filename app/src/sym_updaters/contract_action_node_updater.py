from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import ContractEventName
from app.classes.selection.standard_event_node import ContractActionNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

# TODO: Could generalize this to a "leaf" updater
## Since it just starts off the updater_package value
class ContractActionNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: ContractActionNode, value: any) -> UpdatePackage:
        return UpdatePackage(new_value=node.value)
