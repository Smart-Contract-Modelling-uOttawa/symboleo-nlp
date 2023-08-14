from enum import Enum

class PatternVariable(Enum):
    DATE = 'DATE'
    DATE2 = 'DATE2'
    EVENT = 'EVENT'
    CUSTOM_EVENT = 'CUSTOM_EVENT'
    CONTRACT_EVENT = 'CONTRACT_EVENT'
    SUBJECT = 'SUBJECT'
    VERB_PHRASE = 'VERB_PHRASE'
    IVP = 'IVP'
    TVP = 'TVP'
    LVP = 'LVP'
    TRANSITIVE_VERB = 'TRANSITIVE_VERB'
    LINKING_VERB = 'LINKING_VERB'
    INTRANSITIVE_VERB = 'INTRANSITIVE_VERB'
    ADVERB = 'ADVERB'
    PREP_PHRASE = 'PREP_PHRASE'
    DIRECT_OBJECT = 'DIRECT_OBJECT'
    INDIRECT_OBJECT = 'INDIRECT_OBJECT'
    PREDICATE = 'PREDICATE'

    POINT_FUNCTION = 'POINT_FUNCTION'
    TIMESPAN = 'TIMESPAN'
    TIME_PERIOD = 'TIME_PERIOD'
    INTERVAL = 'INTERVAL'
    ADV_AND_PP = 'ADV_AND_PP'
    DOBJ_PHRASE = 'DOBJ_PHRASE'
    PRED_PHRASE = 'PRED_PHRASE'

    P_BEFORE_E = 'P_BEFORE_E'
    P_BEFORE_S = 'P_BEFORE_S'
    P_BEFORE_T = 'P_BEFORE_T'
    P_AFTER = 'P_AFTER'
    P_AFTER_E = 'P_AFTER_E'
    P_AFTER_PF = 'P_AFTER_PF'
    P_AFTER_T = 'P_AFTER_T'
    P_AFTER_W = 'P_AFTER_W'
    P_AFTER_I = 'P_AFTER_I'
    P_EXCEPT = 'P_EXCEPT'
    P_DURING = 'P_DURING'

    CONDITIONAL_A = 'CONDITIONAL_A'
    CONDITIONAL_T = 'CONDITIONAL_T'
    CONDITIONAL_N = 'CONDITIONAL_N'

    NOTICE_EVENT = 'NOTICE_EVENT'

    AFTER = 'AFTER'
    AND = 'AND'
    BETWEEN = 'BETWEEN'
    FOR = 'FOR'
    FROM = 'FROM'
    WITHIN = 'WITHIN'
    UNTIL = 'UNTIL'

    TIMESPAN_PIECES = 'TIMESPAN_PIECES'
