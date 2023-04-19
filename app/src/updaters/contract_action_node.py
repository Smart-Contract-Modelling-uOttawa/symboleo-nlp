from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.other.contract_update_obj import UpdatePackage
from app.src.updaters.iupdate_package import IUpdatePackage
from app.classes.other.frame_event import FrameEvent

class ContractActionNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            value.verb = node.value 
            return UpdatePackage(new_value=value)
        else:
            new_value = FrameEvent()
            new_value.verb = node.value
            return UpdatePackage(new_value=new_value)
