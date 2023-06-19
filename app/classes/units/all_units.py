from typing import Dict, Type
from app.classes.units.unit_type import UnitType
from app.classes.units.input_unit import InputUnit, DummyUnit
from app.classes.units.before_unit import BeforeUnit
from app.classes.units.date_unit import DateUnit
from app.classes.units.event_unit import EventUnit
from app.classes.units.root_unit import RootUnit
from app.classes.units.timespan_unit import TimespanUnit
from app.classes.units.within_unit import WithinUnit
from app.classes.units.if_unit import IfUnit
from app.classes.units.when_unit import WhenUnit
from app.classes.units.after_unit import AfterUnit
from app.classes.units.until_unit import UntilUnit
from app.classes.units.unless_unit import UnlessUnit
from app.classes.units.for_unit import ForUnit
from app.classes.units.of_unit import OfUnit
from app.classes.units.following_unit import FollowingUnit
from app.classes.units.timepoint_unit import TimepointUnit
from app.classes.units.custom_event_units import *
from app.classes.units.standard_event_units import *
from app.classes.units.fails_to_unit import FailsToUnit


unit_type_dict: Dict[UnitType, Type[InputUnit]] = {
    UnitType.ROOT: RootUnit,
    UnitType.DATE: DateUnit,
    UnitType.EVENT: EventUnit,
    UnitType.TIMESPAN: TimespanUnit,
    UnitType.BEFORE: BeforeUnit,
    UnitType.WITHIN: WithinUnit,
    UnitType.IF: IfUnit,
    UnitType.WHEN: WhenUnit,
    UnitType.DUMMY: DummyUnit,
    UnitType.AFTER: AfterUnit,
    UnitType.UNTIL: UntilUnit,
    UnitType.UNLESS: UnlessUnit,
    UnitType.FOR: ForUnit,
    UnitType.FOLLOWING: FollowingUnit,
    UnitType.OF: OfUnit,

    UnitType.TIMEPOINT: TimepointUnit,
    #UnitType.DOMAIN_TIMEPOINT: DomainTimepointUnit,
    UnitType.CUSTOM_EVENT: CustomEventUnit,
    UnitType.ADVERB: AdverbUnit,
    UnitType.STANDARD_EVENT: StandardEventUnit,
    UnitType.FAILS_TO: FailsToUnit,
    UnitType.VERB: VerbUnit,
    UnitType.TRANSITIVE_VERB: TransitiveVerbUnit,
    UnitType.INTRANSITIVE_VERB: IntransitiveVerbUnit,
    UnitType.LINKING_VERB: LinkingVerbUnit,
    UnitType.SUBJECT: SubjectUnit,
    UnitType.DOBJ: DobjUnit,
    UnitType.PREDICATE: PredicateUnit,
    UnitType.PREP_PHRASE: PrepUnit,

    UnitType.STANDARD_EVENT: StandardEventUnit,
    UnitType.CONTRACT_EVENT: ContractEventUnit,
    UnitType.CONTRACT_ACTION: ContractActionUnit,
    UnitType.CONTRACT_SUBJECT: ContractSubjectUnit,

    UnitType.NORM_EVENT: NormEventUnit,
    UnitType.OBLIGATION_SUBJECT: ObligationSubjectUnit,
    UnitType.OBLIGATION_ACTION: ObligationActionUnit,

    UnitType.FINAL_NODE: FinalUnit


    ####...
}
