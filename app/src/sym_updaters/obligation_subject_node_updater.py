from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import ObligationEventName, ObligationEvent
from app.classes.selection.standard_event_node import ObligationSubjectNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

class ObligationSubjectNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: ObligationSubjectNode, value: any) -> UpdatePackage:
            if isinstance(value, ObligationEventName):
                new_value = ObligationEvent(value, node.value.str_val)
                return UpdatePackage(new_value=new_value)
