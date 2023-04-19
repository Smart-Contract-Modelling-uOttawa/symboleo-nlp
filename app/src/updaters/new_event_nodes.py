from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.other.contract_update_obj import UpdatePackage
from app.src.updaters.iupdate_package import IUpdatePackage
from app.classes.other.frame_event import FrameEvent


class SubjectUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            value.subj = node.value 
            return UpdatePackage(new_value=value)
    
class VerbUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            value.verb = node.value 
            return UpdatePackage(new_value=value)

class DobjUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            value.dobj = node.value 
            return UpdatePackage(new_value=value)
        else:
            new_value = FrameEvent()
            new_value.dobj = node.value
            return UpdatePackage(new_value=new_value)

class PredicateUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            value.predicate = node.value 
            return UpdatePackage(new_value=value)
        else:
            new_value = FrameEvent()
            new_value.predicate = node.value
            return UpdatePackage(new_value=new_value)

class AdverbUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            value.adverb = node.value 
            return UpdatePackage(new_value=value)
        else:
            new_value = FrameEvent()
            new_value.adverb = node.value
            return UpdatePackage(new_value=new_value)


class PPUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            value.pps.append(node.value) 
            return UpdatePackage(new_value=value)
        else:
            new_value = FrameEvent()
            new_value.pps = [node.value]
            return UpdatePackage(new_value=new_value)
