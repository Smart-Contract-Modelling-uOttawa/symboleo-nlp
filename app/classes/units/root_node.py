from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.if_node import IfNode
from app.classes.units.before_node import BeforeNode
from app.classes.units.until_node import UntilNode
from app.classes.units.within_node import WithinNode
from app.classes.units.after_node import AfterNode

from app.classes.elements.root_node import RootNode as Target

class RootNode(InputUnit):
    node_type = UnitType.ROOT
    sn_type = Target
    children = [IfNode, BeforeNode, UntilNode, WithinNode, AfterNode]
