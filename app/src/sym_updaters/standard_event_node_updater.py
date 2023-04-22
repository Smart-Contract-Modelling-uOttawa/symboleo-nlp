from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import ContractEvent, ContractEventName, ObligationEvent, ObligationEventName
from app.classes.selection.selected_node import SelectedNode
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage
from app.classes.custom_event.custom_event import CustomEvent

class StandardEventNodeUpdater(IUpdatePackage):
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        # Will likely have a separate event here (StandardEvent...) to take care of this
        ## Dont want to re-parse thigns out. Will have a separate thing...
        if type(value) == CustomEvent:
            if value.subj.str_val == 'contract':
                c_event_name = ContractEventName[str(value.verb.verb_str).capitalize()]
                new_value = ContractEvent(c_event_name)

            elif 'obligation' in value.subj.str_val.lower():
                o_event_name = ObligationEventName[str(value.verb.verb_str).capitalize()]
                # Will clean this up
                o_name = value.subj.str_val.lower().split(' ')[0]
                new_value = ObligationEvent(o_event_name, o_name)

            return UpdatePackage(new_value = new_value)
        

