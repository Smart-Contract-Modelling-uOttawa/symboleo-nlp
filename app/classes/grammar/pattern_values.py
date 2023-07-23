from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.units.all_units import UnitType

class GOr:
    def __init__(self, *args):
        self.args = args

class GAnd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# TODO: Prob rename this. Its pretty important
temp_tree = {
    PV.P_BEFORE_S: GOr(UnitType.BEFORE, UnitType.BY), 
    PV.P_BEFORE_T: GOr(UnitType.BEFORE, UnitType.PRIOR_TO), 
    PV.P_BEFORE_E: GOr(UnitType.BEFORE, UnitType.PRIOR_TO), #...
    
    PV.P_AFTER_W: GOr(UnitType.AFTER, UnitType.FOLLOWING, UnitType.FROM, UnitType.OF),
    PV.P_AFTER_T: GOr(UnitType.AFTER, UnitType.FOLLOWING, UnitType.FROM),
    PV.P_AFTER_E: GOr(UnitType.AFTER),
    PV.P_AFTER: GOr(UnitType.AFTER, UnitType.LATER_THAN),
    PV.P_AFTER_PF: GOr(UnitType.FOLLOWING),

    PV.P_EXCEPTION: GOr(UnitType.WITHOUT, UnitType.UNLESS, UnitType.EXCEPT),
    PV.CONDITIONAL_T: GOr(UnitType.WHEN),
    PV.CONDITIONAL_A: GOr(UnitType.IF, UnitType.AFTER, UnitType.IN_EVENT, UnitType.IN_CASE, UnitType.ONCE, UnitType.UPON),
    PV.CONDITIONAL_N: GOr(UnitType.UPON, UnitType.WITH, UnitType.BY_GIVING),

    PV.WITHIN: UnitType.WITHIN,
    PV.UNTIL: UnitType.UNTIL,

    PV.TIMESPAN: UnitType.TIMESPAN,
    PV.DATE: UnitType.DATE,
    PV.TIME_PERIOD: UnitType.TIME_PERIOD,

    PV.EVENT: GAnd(UnitType.EVENT, GOr(PV.CUSTOM_EVENT, PV.CONTRACT_EVENT, PV.NORM_EVENT)),
    PV.CUSTOM_EVENT: GAnd(UnitType.CUSTOM_EVENT, GAnd(UnitType.SUBJECT, PV.VERB_PHRASE)),
    PV.CONTRACT_EVENT: GAnd(UnitType.CONTRACT_EVENT, GAnd(UnitType.CONTRACT_SUBJECT, UnitType.CONTRACT_ACTION)),
    PV.NORM_EVENT: GAnd(UnitType.NORM_EVENT, GAnd(UnitType.OBLIGATION_SUBJECT, UnitType.OBLIGATION_ACTION)),
    PV.NOTICE_EVENT: UnitType.NOTICE_EVENT,

    PV.VERB_PHRASE: GOr(PV.IVP, PV.TVP, PV.LVP),
    PV.IVP: GAnd(UnitType.INTRANSITIVE_VERB, PV.ADV_AND_PP),
    PV.TVP: GAnd(UnitType.TRANSITIVE_VERB, PV.DOBJ_PHRASE),
    PV.LVP: GAnd(UnitType.LINKING_VERB, PV.PRED_PHRASE),
    PV.DOBJ_PHRASE: GAnd(UnitType.DOBJ, PV.ADV_AND_PP),
    PV.ADV_AND_PP: GOr(UnitType.FINAL_NODE, GAnd(UnitType.ADVERB, UnitType.PREP_PHRASE), UnitType.PREP_PHRASE),
    PV.PRED_PHRASE: GAnd(UnitType.PREDICATE, PV.ADV_AND_PP),
    # Prep phrase...?

    PV.INTERVAL: GOr(
        GAnd(PV.BETWEEN_TIMEPOINT, PV.AND_TIMEPOINT),
        GAnd(PV.FROM_TIMEPOINT, PV.UNTIL_TIMEPOINT),
        GAnd(PV.P_DURING, UnitType.TIME_PERIOD),
        GAnd(PV.FOR_TIMESPAN, PV.AFTER_TIMEPOINT),
    ),
    PV.BETWEEN_TIMEPOINT: GAnd(UnitType.BETWEEN, UnitType.TIMEPOINT),
    PV.AND_TIMEPOINT: GAnd(UnitType.AND, UnitType.TIMEPOINT),
    PV.FROM_TIMEPOINT: GAnd(UnitType.FROM, UnitType.TIMEPOINT),
    PV.UNTIL_TIMEPOINT: GAnd(UnitType.UNTIL, UnitType.TIMEPOINT),
    PV.P_DURING: GOr(UnitType.DURING, UnitType.THROUGHOUT, UnitType.WITHIN),
    PV.FOR_TIMESPAN: GAnd(UnitType.FOR, UnitType.TIMESPAN),
    PV.AFTER_TIMEPOINT: GAnd(PV.P_AFTER_I, UnitType.TIMEPOINT),
    PV.P_AFTER_I: GOr(UnitType.FOLLOWING, UnitType.AFTER)
}
