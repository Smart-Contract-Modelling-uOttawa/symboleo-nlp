from typing import Dict, Type
from app.classes.tokens.node_type import NodeType
from app.classes.selection.selected_node import SelectedNode, DummyNode
from app.classes.selection.before_node import BeforeNode
from app.classes.selection.contract_event_action_node import ContractEventActionNode
from app.classes.selection.contract_event_node import ContractEventNode
from app.classes.selection.date_node import DateNode
from app.classes.selection.domain_event_name_node import DomainEventNameNode
from app.classes.selection.domain_event_node import DomainEventNode
from app.classes.selection.event_node import EventNode
from app.classes.selection.obligation_event_action_node import ObligationEventActionNode
from app.classes.selection.obligation_event_node import ObligationEventNode
from app.classes.selection.obligation_event_var_node import ObligationEventVarNode
from app.classes.selection.root_node import RootNode
from app.classes.selection.timespan_node import TimespanNode
from app.classes.selection.within_node import WithinNode
from app.classes.selection.if_node import IfNode
from app.classes.selection.state_node import StateNode
from app.classes.selection.after_node import AfterNode
from app.classes.selection.until_node import UntilNode
from app.classes.selection.using_node import UsingNode
from app.classes.selection.instrument_node import InstrumentNode
from app.classes.selection.timepoint_node import TimepointNode
from app.classes.selection.domain_timepoint_node import DomainTimepointNode


node_type_to_class: Dict[NodeType, Type[SelectedNode]] = {
    NodeType.ROOT: RootNode,
    NodeType.CONTRACT_EVENT: ContractEventNode,
    NodeType.CONTRACT_EVENT_ACTION: ContractEventActionNode,
    NodeType.DATE: DateNode,
    NodeType.DOMAIN_EVENT: DomainEventNode,
    NodeType.DOMAIN_EVENT_NAME: DomainEventNameNode,
    NodeType.EVENT: EventNode,
    NodeType.OBLIGATION_EVENT: ObligationEventNode,
    NodeType.OBLIGATION_EVENT_ACTION: ObligationEventActionNode,
    NodeType.OBLIGATION_EVENT_VAR: ObligationEventVarNode,
    NodeType.TIMESPAN: TimespanNode,
    NodeType.BEFORE: BeforeNode,
    NodeType.WITHIN: WithinNode,
    NodeType.IF: IfNode,
    NodeType.STATE: StateNode,
    NodeType.DUMMY: DummyNode,
    NodeType.AFTER: AfterNode,
    NodeType.UNTIL: UntilNode,
    NodeType.USING: UsingNode,
    NodeType.INSTRUMENT: InstrumentNode,
    NodeType.TIMEPOINT: TimepointNode,
    NodeType.DOMAIN_TIMEPOINT: DomainTimepointNode
    ####...
}
