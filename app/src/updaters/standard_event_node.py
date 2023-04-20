from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import ContractEvent, ContractEventName, ObligationEvent, ObligationEventName
from app.classes.selection.selected_node import SelectedNode
from app.classes.other.contract_update_obj import UpdatePackage
from app.src.updaters.iupdate_package import IUpdatePackage
from app.classes.other.frame_event import FrameEvent

class StandardEventNodeUpdater(IUpdatePackage):

    # I could also set up the possibility for the node value itself...
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        # Will likely have a separate event here (StandardEvent...) to take care of this
        ## Dont want to re-parse thigns out. Will have a separate thing...
        if type(value) == FrameEvent:
            if value.subj.subj_str == 'contract':
                c_event_name = ContractEventName[str(value.verb.verb_str).capitalize()]
                new_value = ContractEvent(c_event_name)

            elif 'obligation' in value.subj.subj_str.lower():
                o_event_name = ObligationEventName[str(value.verb.verb_str).capitalize()]
                # Will clean this up
                o_name = value.subj.subj_str.lower().split(' ')[0]
                new_value = ObligationEvent(o_event_name, o_name)

            return UpdatePackage(new_value = new_value)
        

