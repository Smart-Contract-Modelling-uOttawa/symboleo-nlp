from app.classes.processing.case_obj import CasePattern
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensAfter, PredicateFunctionWHappensBefore, PredicateFunctionWHappensBeforeEvent

# case patterns, defaults, etc...
def get_tf_patterns(nlp):

    # Cases
    within_time_period = [
        [{"LOWER": {'IN': ['within']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    before_date = [
        [{"LOWER": {'IN': ['before', 'by', 'on']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    # This is where I add my own preprocessing to pick up domain events...
    ## An event may be more than just a token though...
    before_event = [
        [{"LOWER": {'IN': ['before']}}, {"LOWER": 'the', "OP": "?"}, {"ENT_TYPE": 'DOMAIN_EVENT', "OP": "+"}],
    ]

    after_date = [
        [{"LOWER": {'IN': ['after']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    between_dates = [
        [{"LOWER": {'IN': ['between']}}, {"ENT_TYPE": 'DATE', "OP": "+"}, {"LOWER": "and"}, {"ENT_TYPE": 'DATE', "OP": "+"} ],
    ]

    until_adp_event = [
        [{"LOWER": {'IN': ['until']}}, {"ENT_TYPE": 'DATE', "OP": "+"}, {"LOWER": {'IN': ['after']}, "POS": "ADP"}, {"ENT_TYPE": "DOMAIN_EVENT", "OP": "+"} ],
    ]

    case_patterns = [
        CasePattern(within_time_period, PredicateFunctionWHappensBefore),
        CasePattern(before_date, PredicateFunctionWHappensBefore),
        CasePattern(after_date, PredicateFunctionHappensAfter),
        CasePattern(before_event, PredicateFunctionWHappensBeforeEvent),
        #CasePattern(between_dates, ),
        CasePattern(until_adp_event, PredicateFunctionWHappensBefore)
    ]

    return case_patterns

    
