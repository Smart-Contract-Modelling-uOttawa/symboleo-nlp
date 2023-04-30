from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

class FinalNode(AbstractNode):
    node_type = NodeType.FINAL_NODE
    prompt = 'FINISH'
    needs_value = False
    init_value = 'X'
