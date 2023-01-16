from typing import Dict, Type
from app.classes.grammar.node_type import NodeType
from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.grammar_nodes.before_node import BeforeNode
from app.classes.grammar.grammar_nodes.contract_event_action_node import ContractEventActionNode
from app.classes.grammar.grammar_nodes.contract_event_node import ContractEventNode
from app.classes.grammar.grammar_nodes.date_node import DateNode
from app.classes.grammar.grammar_nodes.domain_event_name_node import DomainEventNameNode
from app.classes.grammar.grammar_nodes.domain_event_node import DomainEventNode
from app.classes.grammar.grammar_nodes.event_node import EventNode
from app.classes.grammar.grammar_nodes.obligation_event_action_node import ObligationEventActionNode
from app.classes.grammar.grammar_nodes.obligation_event_node import ObligationEventNode
from app.classes.grammar.grammar_nodes.obligation_event_var_node import ObligationEventVarNode
from app.classes.grammar.grammar_nodes.root_node import RootNode
from app.classes.grammar.grammar_nodes.timespan_node import TimespanNode
from app.classes.grammar.grammar_nodes.within_node import WithinNode

