from typing import Dict, Type
from app.classes.units.unit_type import UnitType
from app.classes.units.input_unit import InputUnit, DummyUnit
from app.classes.units.cond_units import *
from app.classes.units.custom_event_units import *
from app.classes.units.other_units import *
from app.classes.units.standard_event_units import *
from app.classes.units.temporal_units import *
from app.classes.units.time_units import *

unit_type_dict: Dict[UnitType, Type[InputUnit]] = {
    UnitType.LATER_THAN: LaterThanUnit,
    UnitType.WITH: WithUnit,
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
    UnitType.EXCEPT: ExceptUnit,
    UnitType.WITHOUT: WithoutUnit,
    UnitType.FOR: ForUnit,
    UnitType.FOLLOWING: FollowingUnit,
    UnitType.OF: OfUnit,
    UnitType.FROM: FromUnit,
    UnitType.PRIOR_TO: PriorToUnit,
    UnitType.BY: ByUnit,
    UnitType.IN_CASE: InCaseUnit,
    UnitType.IN_EVENT: InEventUnit,
    UnitType.ONCE: OnceUnit,
    UnitType.UPON: UponUnit,
    UnitType.BETWEEN: BetweenUnit,
    UnitType.DURING: DuringUnit,
    UnitType.THROUGHOUT: ThroughoutUnit,

    UnitType.TIME_PERIOD: TimePeriodUnit,
    UnitType.TIME_VALUE: TimeValueUnit,
    UnitType.TIME_UNIT: TimeUnitUnit,
    UnitType.CUSTOM_EVENT: CustomEventUnit,
    UnitType.ADVERB: AdverbUnit,
    UnitType.FAILS_TO: FailsToUnit,
    UnitType.NOT: NotUnit,
    UnitType.VERB: VerbUnit,
    UnitType.TRANSITIVE_VERB: TransitiveVerbUnit,
    UnitType.INTRANSITIVE_VERB: IntransitiveVerbUnit,
    UnitType.LINKING_VERB: LinkingVerbUnit,
    UnitType.SUBJECT: SubjectUnit,
    UnitType.DOBJ: DobjUnit,
    UnitType.PREDICATE: PredicateUnit,
    UnitType.PREP_PHRASE: PrepUnit,

    UnitType.CONTRACT_EVENT: ContractEventUnit,
    UnitType.CONTRACT_ACTION: ContractActionUnit,
    UnitType.CONTRACT_SUBJECT: ContractSubjectUnit,

    UnitType.NORM_EVENT: NormEventUnit,
    UnitType.OBLIGATION_SUBJECT: ObligationSubjectUnit,
    UnitType.OBLIGATION_ACTION: ObligationActionUnit,

    UnitType.FINAL_NODE: FinalUnit


    ####...
}
