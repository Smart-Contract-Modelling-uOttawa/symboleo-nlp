from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.selection.selected_node import SelectedNode

from app.classes.units.all_nodes import NormEventNode, ObligationSubjectNode

from app.src.child_getters.child_getter import IGetNodeChildren

class NormEventNodeCG(IGetNodeChildren):
    def get(self, parent_node: NormEventNode, contract: SymboleoContract, prev_value: SelectedNode) -> List[InputUnit]:
        opts = []
        for x in contract.contract_spec.obligations:
            next_ob = contract.contract_spec.obligations[x]
            opts.append(next_ob.id)
        
        node1 = ObligationSubjectNode(opts)

        return [node1]

