from spacy.matcher import Matcher

# May be the exact same as delivery timefrme matcher...
def get_ptf_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    # Validation Patterns
    validation_patterns = [
    ]
    matcher.add('validation', validation_patterns)

    # Cases
    within_time_period_pattern = [
        [{"LOWER": {'IN': ['within']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    before_date_pattern = [
        [{"LOWER": {'IN': ['before', 'by', 'on']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    # This is where I add my own preprocessing to pick up domain events...
    ## An event may be more than just a token though...
    before_event_pattern = [
        [{"LOWER": {'IN': ['before']}}, {"LOWER": 'the', "OP": "?"}, {"ENT_TYPE": 'DOMAIN_EVENT', "OP": "+"}],
    ]

    after_date_pattern = [
        [{"LOWER": {'IN': ['after']}}, {"ENT_TYPE": 'DATE', "OP": "+"}],
    ]

    between_dates_pattern = [
        [{"LOWER": {'IN': ['between']}}, {"ENT_TYPE": 'DATE', "OP": "+"}, {"LOWER": "and"}, {"ENT_TYPE": 'DATE', "OP": "+"} ],
    ]

    matcher.add("within_time_period", within_time_period_pattern)
    matcher.add("before_date", before_date_pattern)
    matcher.add("before_event", before_event_pattern)
    matcher.add("after_date", after_date_pattern)
    matcher.add("between_dates", between_dates_pattern)


    # Primitives
    time_value_pattern = [
        [{"POS": "NUM", "DEP": "nummod", "ENT_TYPE": "DATE" }],
    ]

    time_unit_pattern = [
        [{"POS": "NOUN", "DEP": "pobj" , "ENT_TYPE": "DATE" }],
    ]

    point_vde_pattern = [
        [{"POS": "PROPN", "DEP": "pobj" , "ENT_TYPE": "DATE" }, 
         {"POS": "NUM", "DEP": "nummod" , "ENT_TYPE": "DATE" },
         {"POS": "PUNCT", "DEP": "punct" , "ENT_TYPE": "DATE" },
         {"POS": "NUM", "DEP": "nummod" , "ENT_TYPE": "DATE" }],
    ]

    event_vde_pattern = [
        [{"POS": "VERB", "ENT_TYPE": "DOMAIN_EVENT" }],
    ]

    matcher.add('time_value_int', time_value_pattern)
    matcher.add('time_unit_string', time_unit_pattern)
    matcher.add('point_vde', point_vde_pattern)
    matcher.add('event_vde', event_vde_pattern) # will have separate ones for contract/ob/pow events

    return matcher
