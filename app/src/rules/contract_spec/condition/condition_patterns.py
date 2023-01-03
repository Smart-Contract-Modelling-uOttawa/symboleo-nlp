from app.classes.processing.case_obj import CasePattern
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin, PredicateFunctionOccurs


def get_condition_patterns(nlp):

    # Cases
    if_domain_event_pattern = [
        [{'LOWER': 'if'}, {'ENT_TYPE': 'DOMAIN_EVENT', 'OP': '+'}]
    ]

    until_domain_event_pattern = [
        [{'LOWER': 'until'}, {'ENT_TYPE': 'DOMAIN_EVENT', 'OP': '+'}]
    ]

    unless_pattern = [
        [{'LOWER': 'unless'}]
    ]

    case_patterns = [
        CasePattern(if_domain_event_pattern, PredicateFunctionHappens),
        CasePattern(until_domain_event_pattern, PredicateFunctionHappensWithin),
        CasePattern(unless_pattern, PredicateFunctionOccurs),
    ]

    return case_patterns
