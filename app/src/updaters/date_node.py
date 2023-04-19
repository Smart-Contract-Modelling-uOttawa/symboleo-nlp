from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.other.contract_update_obj import UpdatePackage
from app.src.updaters.iupdate_package import IUpdatePackage

from app.classes.spec.sym_point import PointVDE

class DateNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        return UpdatePackage(new_value = PointVDE(node.value))