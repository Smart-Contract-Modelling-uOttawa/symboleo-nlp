from app.classes.spec.norm import INorm
from app.classes.spec.point_function import TimeUnit
from app.classes.selection.selected_node import SelectedNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

class TimespanNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        # Will need to split up the self.value... maybe just by a space?
        (tvi,tsu)  = node.value.split(' ')
        
        # Or maybe the value will be a dynamic type?
        time_value = tvi
        time_unit = TimeUnit[tsu.capitalize()]

        new_value = {
            'event': value,
            'time_value': time_value,
            'time_unit': time_unit
        }

        return UpdatePackage(new_value = new_value)
    

        