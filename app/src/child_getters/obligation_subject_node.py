from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ObligationEventName
from app.classes.units.input_unit import InputUnit
from app.classes.selection.selected_node import SelectedNode

from app.classes.units.all_nodes import ObligationSubjectNode, ObligationActionNode

from app.src.child_getters.child_getter import IGetNodeChildren

class ObligationSubjectNodeCG(IGetNodeChildren):
    def get(self, parent_node: ObligationSubjectNode, contract: SymboleoContract, prev_value: SelectedNode) -> List[InputUnit]:
        opts = [str(x.value).lower() for x in ObligationEventName]
            
        node1 = ObligationActionNode(opts)

        return [node1]

