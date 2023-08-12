from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.units.all_units import UnitType

class GOr:
    def __init__(self, *args):
        self.args = args

class GAnd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

full_grammar = {
    PV.P_BEFORE_S: GOr(UnitType.BEFORE, UnitType.BY), 
    PV.P_BEFORE_T: GOr(UnitType.BEFORE, UnitType.PRIOR_TO), 
    PV.P_BEFORE_E: GOr(UnitType.BEFORE, UnitType.PRIOR_TO), 
    
    PV.P_AFTER_W: GOr(UnitType.AFTER, UnitType.FOLLOWING, UnitType.FROM, UnitType.OF),
    PV.P_AFTER_T: GOr(UnitType.AFTER, UnitType.FOLLOWING, UnitType.FROM),
    PV.P_AFTER_E: GOr(UnitType.AFTER),
    PV.P_AFTER: GOr(UnitType.AFTER, UnitType.LATER_THAN),
    PV.P_AFTER_PF: GOr(UnitType.FOLLOWING),
    PV.P_AFTER_I: GOr(UnitType.FOLLOWING, UnitType.AFTER),

    PV.P_DURING: GOr(UnitType.DURING, UnitType.THROUGHOUT, UnitType.WITHIN),
    PV.P_EXCEPT: GOr(UnitType.WITHOUT, UnitType.UNLESS, UnitType.EXCEPT),
    
    PV.CONDITIONAL_T: GOr(UnitType.WHEN),
    PV.CONDITIONAL_A: GOr(UnitType.AFTER, UnitType.IF, UnitType.IN_EVENT, UnitType.IN_CASE, UnitType.ONCE, UnitType.UPON),
    PV.CONDITIONAL_N: GOr(UnitType.UPON, UnitType.WITH),

    PV.AFTER: UnitType.AFTER,
    PV.AND: UnitType.AND,
    PV.BETWEEN: UnitType.BETWEEN,
    PV.FOR: UnitType.FOR,
    PV.FROM: UnitType.FROM,
    PV.WITHIN: UnitType.WITHIN,
    PV.UNTIL: UnitType.UNTIL,
    
    PV.TIMESPAN: GAnd(UnitType.TIMESPAN, PV.TIMESPAN_PIECES),
    PV.TIMESPAN_PIECES: GAnd(UnitType.TIME_VALUE, UnitType.TIME_UNIT),

    PV.DATE: UnitType.DATE,
    PV.DATE2: UnitType.DATE,
    PV.TIME_PERIOD: UnitType.TIME_PERIOD,
    
    PV.EVENT: GAnd(UnitType.EVENT, GOr(PV.CUSTOM_EVENT, PV.CONTRACT_EVENT)),
    PV.CUSTOM_EVENT: GAnd(UnitType.CUSTOM_EVENT, GAnd(UnitType.SUBJECT, PV.VERB_PHRASE)),
    PV.CONTRACT_EVENT: GAnd(UnitType.CONTRACT_EVENT, GAnd(UnitType.CONTRACT_SUBJECT, UnitType.CONTRACT_ACTION)),

    PV.VERB_PHRASE: GOr(PV.IVP, PV.TVP, PV.LVP),
    PV.IVP: GAnd(UnitType.INTRANSITIVE_VERB, PV.ADV_AND_PP),
    PV.TVP: GAnd(UnitType.TRANSITIVE_VERB, PV.DOBJ_PHRASE),
    PV.LVP: GAnd(
        UnitType.LINKING_VERB, 
        PV.PRED_PHRASE
    ),
    
    PV.DOBJ_PHRASE: GAnd(UnitType.DOBJ, PV.ADV_AND_PP),
    PV.ADV_AND_PP: GOr(UnitType.FINAL_NODE, GAnd(UnitType.ADVERB, UnitType.PREP_PHRASE), UnitType.PREP_PHRASE),
    PV.PRED_PHRASE: GAnd(
        UnitType.PREDICATE, 
        GOr(
            UnitType.FINAL_NODE,
            UnitType.PREP_PHRASE
        )
    ),
}
