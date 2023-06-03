from typing import Dict, Type
from app.classes.units.unit_type import UnitType
from app.classes.elements.element import Element, DummyElement
from app.classes.elements.static_elements import *
from app.classes.elements.time_elements import *
from app.classes.elements.event_element import EventElement
from app.classes.elements.custom_event_elements import *
from app.classes.elements.standard_event_elements import *


unit_type_to_class: Dict[UnitType, Type[Element]] = {
    UnitType.ROOT: RootElement,
    UnitType.DATE: DateElement,
    UnitType.EVENT: EventElement,
    UnitType.TIMESPAN: TimespanElement,
    UnitType.BEFORE: BeforeElement,
    UnitType.WITHIN: WithinElement,
    UnitType.IF: IfElement,
    UnitType.WHEN: WhenElement,
    UnitType.DUMMY: DummyElement,
    UnitType.AFTER: AfterElement,
    UnitType.UNTIL: UntilElement,
    UnitType.UNLESS: UnlessElement,
    UnitType.FOR: ForElement,
    UnitType.FOLLOWING: FollowingElement,
    UnitType.OF: OfElement,

    UnitType.TIMEPOINT: TimepointElement,
    UnitType.DOMAIN_TIMEPOINT: DomainTimepointElement,
    UnitType.CUSTOM_EVENT: CustomEventElement,
    UnitType.ADVERB: AdverbElement,
    UnitType.STANDARD_EVENT: StandardEventElement,
    UnitType.FAILS_TO: FailsToElement,
    UnitType.VERB: VerbElement,
    UnitType.SUBJECT: SubjectElement,
    UnitType.DOBJ: DobjElement,
    UnitType.PREDICATE: PredicateElement,
    UnitType.PREP_PHRASE: PrepElement,

    UnitType.STANDARD_EVENT: StandardEventElement,
    UnitType.CONTRACT_EVENT: ContractEventElement,
    UnitType.CONTRACT_ACTION: ContractActionElement,
    UnitType.CONTRACT_SUBJECT: ContractSubjectElement,

    UnitType.NORM_EVENT: NormEventElement,
    UnitType.OBLIGATION_SUBJECT: ObligationSubjectElement,
    UnitType.OBLIGATION_ACTION: ObligationActionElement,

    UnitType.FINAL_NODE: FinalElement


    ####...
}
