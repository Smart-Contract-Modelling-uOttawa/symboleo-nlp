from typing import Dict, Type
from app.classes.grammar.node_type import NodeType
from app.classes.grammar.selected_node import SelectedNode, DummyNode
from app.classes.grammar.selected_nodes.before_node import BeforeNode
from app.classes.grammar.selected_nodes.contract_event_action_node import ContractEventActionNode
from app.classes.grammar.selected_nodes.contract_event_node import ContractEventNode
from app.classes.grammar.selected_nodes.date_node import DateNode
from app.classes.grammar.selected_nodes.domain_event_name_node import DomainEventNameNode
from app.classes.grammar.selected_nodes.domain_event_node import DomainEventNode
from app.classes.grammar.selected_nodes.event_node import EventNode
from app.classes.grammar.selected_nodes.obligation_event_action_node import ObligationEventActionNode
from app.classes.grammar.selected_nodes.obligation_event_node import ObligationEventNode
from app.classes.grammar.selected_nodes.obligation_event_var_node import ObligationEventVarNode
from app.classes.grammar.selected_nodes.root_node import RootNode
from app.classes.grammar.selected_nodes.timespan_node import TimespanNode
from app.classes.grammar.selected_nodes.within_node import WithinNode
from app.classes.grammar.selected_nodes.if_node import IfNode
from app.classes.grammar.selected_nodes.state_node import StateNode
from app.classes.grammar.selected_nodes.after_node import AfterNode
from app.classes.grammar.selected_nodes.until_node import UntilNode
from app.classes.grammar.selected_nodes.using_node import UsingNode
from app.classes.grammar.selected_nodes.instrument_node import InstrumentNode
from app.classes.grammar.selected_nodes.timepoint_node import TimepointNode
from app.classes.grammar.selected_nodes.domain_timepoint_node import DomainTimepointNode


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
