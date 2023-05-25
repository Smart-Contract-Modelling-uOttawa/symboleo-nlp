from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

from app.classes.spec.sym_point import Point, PointVDE

class DateNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        return UpdatePackage(new_value = Point(PointVDE(node.value)))