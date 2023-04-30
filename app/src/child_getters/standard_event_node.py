from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.selection.selected_node import SelectedNode

from app.classes.tokens.all_nodes import StandardEventNode, ContractEventNode, NormEventNode, CommonEventNode

from app.src.child_getters.child_getter import IGetNodeChildren

from app.classes.template_event.common_event_dict import COMMON_EVENT_DICT

class StandardEventNodeCG(IGetNodeChildren):
    def get(self, parent_node: StandardEventNode, contract: ISymboleoContract, prev_value: SelectedNode) -> List[AbstractNode]:
        contract_event_node = ContractEventNode()

        norm_event_node = NormEventNode(['obligation', 'power'])
    
        common_events = list(COMMON_EVENT_DICT.keys())
        common_event_node = CommonEventNode(common_events)

        return [contract_event_node, norm_event_node, common_event_node]

