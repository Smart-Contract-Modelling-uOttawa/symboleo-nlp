from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage
from app.classes.custom_event.custom_event import CustomEvent

class SubjectUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == CustomEvent:
            value.subj = node.value 
            return UpdatePackage(new_value=value)
    
class VerbUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == CustomEvent:
            value.verb = node.value
            return UpdatePackage(new_value=value)

class DobjUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == CustomEvent:
            value.dobj = node.value 
            return UpdatePackage(new_value=value)
        else:
            new_value = CustomEvent()
            new_value.dobj = node.value
            return UpdatePackage(new_value=new_value)

class PredicateUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == CustomEvent:
            value.predicate = node.value 
            return UpdatePackage(new_value=value)
        else:
            new_value = CustomEvent()
            new_value.predicate = node.value
            return UpdatePackage(new_value=new_value)

class AdverbUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == CustomEvent:
            value.adverb = node.value 
            return UpdatePackage(new_value=value)
        else:
            new_value = CustomEvent()
            new_value.adverb = node.value
            return UpdatePackage(new_value=new_value)


class PPUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: any) -> UpdatePackage:
        if type(value) == CustomEvent:
            value.pps.append(node.value) 
            return UpdatePackage(new_value=value)
        else:
            new_value = CustomEvent()
            new_value.pps = [node.value]
            return UpdatePackage(new_value=new_value)
