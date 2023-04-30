from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.selection.selected_node import SelectedNode

from app.classes.tokens.all_nodes import NormEventNode, ObligationSubjectNode

from app.src.child_getters.child_getter import IGetNodeChildren

class NormEventNodeCG(IGetNodeChildren):
    def get(self, parent_node: NormEventNode, contract: SymboleoContract, prev_value: SelectedNode) -> List[AbstractNode]:
        opts = []
        for x in contract.contract_spec.obligations:
            next_ob = contract.contract_spec.obligations[x]
            opts.append(next_ob.id)
        
        node1 = ObligationSubjectNode(opts)

        return [node1]

