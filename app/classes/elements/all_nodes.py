from typing import Dict, Type
from app.classes.units.unit_type import UnitType
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

node_type_to_class: Dict[UnitType, Type[Element]] = {
    UnitType.ROOT: RootNode,
    UnitType.DATE: DateNode,
    UnitType.EVENT: EventNode,
    UnitType.TIMESPAN: TimespanNode,
    UnitType.BEFORE: BeforeNode,
    UnitType.WITHIN: WithinNode,
    UnitType.IF: IfNode,
    UnitType.DUMMY: DummyNode,
    UnitType.AFTER: AfterNode,
    UnitType.UNTIL: UntilNode,
    UnitType.TIMEPOINT: TimepointNode,
    UnitType.DOMAIN_TIMEPOINT: DomainTimepointNode,
    UnitType.CUSTOM_EVENT: CustomEventNode,
    UnitType.ADVERB: AdverbNode,
    UnitType.STANDARD_EVENT: StandardEventNode,
    UnitType.FAILS_TO: FailsToNode,
    UnitType.VERB: VerbNode,
    UnitType.SUBJECT: SubjectNode,
    UnitType.DOBJ: DobjNode,
    UnitType.PREDICATE: PredicateNode,
    UnitType.PREP_PHRASE: PrepNode,

    UnitType.STANDARD_EVENT: StandardEventNode,
    UnitType.COMMON_EVENT: CommonEventNode,
    UnitType.CONTRACT_EVENT: ContractEventNode,
    UnitType.CONTRACT_ACTION: ContractActionNode,
    UnitType.CONTRACT_SUBJECT: ContractSubjectNode,

    UnitType.NORM_EVENT: NormEventNode,
    UnitType.OBLIGATION_SUBJECT: ObligationSubjectNode,
    UnitType.OBLIGATION_ACTION: ObligationActionNode,

    UnitType.FINAL_NODE: FinalNode

    ####...
}
