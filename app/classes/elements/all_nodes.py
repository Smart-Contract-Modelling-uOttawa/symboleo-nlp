from typing import Dict, Type
from app.classes.units.node_type import NodeType
from app.classes.elements.element import Element, DummyNode
from app.classes.elements.before_node import BeforeNode
from app.classes.elements.date_node import DateNode
from app.classes.elements.event_node import EventNode
from app.classes.elements.root_node import RootNode
from app.classes.elements.timespan_node import TimespanNode
from app.classes.elements.within_node import WithinNode
from app.classes.elements.if_node import IfNode
from app.classes.elements.after_node import AfterNode
from app.classes.elements.until_node import UntilNode
from app.classes.elements.timepoint_node import TimepointNode
from app.classes.elements.domain_timepoint_node import DomainTimepointNode
from app.classes.elements.custom_event_node import *
from app.classes.elements.standard_event_node import *
from app.classes.elements.final_node import *

# Might move all the nodes to this file

node_type_to_class: Dict[NodeType, Type[Element]] = {
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
    NodeType.CUSTOM_EVENT: CustomEventNode,
    NodeType.ADVERB: AdverbNode,
    NodeType.STANDARD_EVENT: StandardEventNode,
    NodeType.FAILS_TO: FailsToNode,
    NodeType.VERB: VerbNode,
    NodeType.SUBJECT: SubjectNode,
    NodeType.DOBJ: DobjNode,
    NodeType.PREDICATE: PredicateNode,
    NodeType.PREP_PHRASE: PrepNode,

    NodeType.STANDARD_EVENT: StandardEventNode,
    NodeType.COMMON_EVENT: CommonEventNode,
    NodeType.CONTRACT_EVENT: ContractEventNode,
    NodeType.CONTRACT_ACTION: ContractActionNode,
    NodeType.CONTRACT_SUBJECT: ContractSubjectNode,

    NodeType.NORM_EVENT: NormEventNode,
    NodeType.OBLIGATION_SUBJECT: ObligationSubjectNode,
    NodeType.OBLIGATION_ACTION: ObligationActionNode,

    NodeType.FINAL_NODE: FinalNode

    ####...
}
