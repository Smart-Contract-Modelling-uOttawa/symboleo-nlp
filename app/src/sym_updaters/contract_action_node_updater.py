from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage
from app.classes.custom_event.custom_event import CustomEvent

class ContractActionNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        if type(value) == CustomEvent:
            value.verb = node.value 
            return UpdatePackage(new_value=value)
        else:
            new_value = CustomEvent()
            new_value.verb = node.value
            return UpdatePackage(new_value=new_value)
