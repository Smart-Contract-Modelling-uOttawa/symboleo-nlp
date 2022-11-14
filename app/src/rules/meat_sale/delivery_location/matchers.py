from spacy.matcher import Matcher

def get_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    basic_pattern = [
        [
            { "POS": "ADP", "LOWER": {'IN': ['at', 'to'] }, "IS_SENT_START": True }, 
            { "OP": "*"},
            { "DEP": "pobj" }
        ]
    ]

    # at the warehouse
    # basic_pattern2 = [
    #     [
    #         { "POS": "ADP", "LOWER": {'IN': ['at', 'to'] } }, 
    #         { "POS": "DET", "OP": "?"},
    #         { "POS": "NOUN", "OP": "+" }
    #     ]
    # ]

    # at their warehouse
    basic_poss_pattern = [
        [
            { "POS": "ADP", "LOWER": {'IN': ['at', 'to'] } }, 
            { "POS": "PRON", "DEP": "poss" },
            { "POS": "NOUN", "OP": "+" }
        ]
    ]

    matcher.add('basic', basic_pattern)
    matcher.add('basic_poss', basic_poss_pattern)

    return matcher
    