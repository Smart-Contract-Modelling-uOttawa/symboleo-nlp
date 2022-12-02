from spacy.matcher import Matcher

# Can combine different spacy approaches - doesnt need to just be one
# e.g. combine the token matcher with the dependency matcher
# Some are for validation, some are for extracting specific props, some are for control flow.


# Will probably make this a class with some more rules and properties
## Three key matches: validation, cases, primitives
## Although validation may be covered by cases...
def get_condition_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    # Validation Patterns
    validation_patterns = [
    ]
    matcher.add('validation', validation_patterns)

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

    matcher.add("if_domain_event", if_domain_event_pattern)
    matcher.add("until_domain_event", until_domain_event_pattern)
    matcher.add("unless", unless_pattern)

    return matcher
