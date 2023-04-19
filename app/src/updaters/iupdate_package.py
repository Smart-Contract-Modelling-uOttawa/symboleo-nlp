from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.other.contract_update_obj import UpdatePackage

class IUpdatePackage:
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        raise NotImplementedError()


class DefaultUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        return UpdatePackage(new_value = value)