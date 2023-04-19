from typing import Dict, Type
from app.classes.tokens.node_type import NodeType
from app.classes.selection.selected_node import SelectedNode, DummyNode
from app.classes.selection.before_node import BeforeNode
from app.classes.selection.date_node import DateNode
from app.classes.selection.event_node import EventNode
from app.classes.selection.root_node import RootNode
from app.classes.selection.timespan_node import TimespanNode
from app.classes.selection.within_node import WithinNode
from app.classes.selection.if_node import IfNode
from app.classes.selection.after_node import AfterNode
from app.classes.selection.until_node import UntilNode
from app.classes.selection.timepoint_node import TimepointNode
from app.classes.selection.domain_timepoint_node import DomainTimepointNode
from app.classes.selection.new_event_node import NewEventNode
from app.classes.selection.standard_event_node import StandardEventNode
from app.classes.selection.contract_action_node import ContractActionNode
from app.classes.selection.contract_subject_node import ContractSubjectNode
from app.classes.selection.new_event_nodes import *

# TODO: May not need this. Might combine the Token and SelectedNode
node_type_to_class: Dict[NodeType, Type[SelectedNode]] = {
    NodeType.ROOT: RootNode,
    NodeType.DATE: DateNode,
    NodeType.EVENT: EventNode,
    NodeType.TIMESPAN: TimespanNode,
    NodeType.BEFORE: BeforeNode,
    NodeType.WITHIN: WithinNode,
    NodeType.IF: IfNode,
    NodeType.DUMMY: DummyNode,
    NodeType.AFTER: AfterNode,
    NodeType.UNTIL: UntilNode,
    NodeType.TIMEPOINT: TimepointNode,
    NodeType.DOMAIN_TIMEPOINT: DomainTimepointNode,
    NodeType.NEW_EVENT: NewEventNode,
    NodeType.STANDARD_EVENT: StandardEventNode
    ####...
}
