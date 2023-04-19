from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.selection.date_node import DateNode as Target

class DateNode(AbstractNode):
    node_type = NodeType.DATE
    sn_type = Target
    prompt = 'Enter a date'
    needs_value = True
