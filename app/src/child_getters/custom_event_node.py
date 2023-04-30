from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.spec.sym_event import ObligationEventName
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.selection.selected_node import SelectedNode

from app.classes.tokens.all_nodes import CustomEventNode, SubjectNode

from app.src.child_getters.child_getter import IGetNodeChildren

class CustomEventNodeCG(IGetNodeChildren):
    def get(self, parent_node: CustomEventNode, contract: SymboleoContract, prev_value: SelectedNode) -> List[AbstractNode]:
        opts = [str(x.value).lower() for x in ObligationEventName]
            
        decls: List[Declaration] = contract.contract_spec.declarations.values()
        roles = [x.name for x in decls if x.base_type == 'roles']
        assets = [x.name for x in decls if x.base_type == 'assets']
        
        subj_children = roles + assets

        return [
            SubjectNode(subj_children)
        ]


