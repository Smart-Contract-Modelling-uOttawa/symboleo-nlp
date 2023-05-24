from app.classes.spec.norm import INorm
from app.classes.selection.selected_node import SelectedNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage
from app.classes.custom_event.custom_event import CustomEvent

# TODO: Id actually like to get rid of these. Would ideally just pass along the entire Event object
## Rather than passing along all the components. Would make things so much easier I think..
## And shouldnt be too hard to implement...
## Would get rid of all the SelectedNodes related to custom event potentially...

class SubjectUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: CustomEvent) -> UpdatePackage:
        value.subj = node.value 
        return UpdatePackage(new_value=value)
    
class VerbUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: CustomEvent) -> UpdatePackage:
        value.verb = node.value
        return UpdatePackage(new_value=value)

class DobjUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: CustomEvent) -> UpdatePackage:
        value.dobj = node.value 
        return UpdatePackage(new_value=value)

class PredicateUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: CustomEvent) -> UpdatePackage:
        value.predicate = node.value 
        return UpdatePackage(new_value=value)

class AdverbUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: CustomEvent) -> UpdatePackage:
        value.adverb = node.value 
        return UpdatePackage(new_value=value)


class PPUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode, value: CustomEvent) -> UpdatePackage:
        if value.pps:
            value.pps.append(node.value) 
        else:
            value.pps = [node.value]
        return UpdatePackage(new_value=value)
        