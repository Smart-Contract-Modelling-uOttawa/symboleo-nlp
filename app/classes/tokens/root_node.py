from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.if_node import IfNode
from app.classes.tokens.before_node import BeforeNode
from app.classes.tokens.until_node import UntilNode
from app.classes.tokens.within_node import WithinNode
from app.classes.tokens.after_node import AfterNode

from app.classes.selection.root_node import RootNode as Target

class RootNode(AbstractNode):
    node_type = NodeType.ROOT
    sn_type = Target
    children = [IfNode, BeforeNode, UntilNode, WithinNode, AfterNode]
