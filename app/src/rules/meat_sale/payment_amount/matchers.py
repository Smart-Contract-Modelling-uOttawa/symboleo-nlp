from spacy.matcher import Matcher

def get_validation_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    validation_pattern = [
        [
            { "POS": "NUM" }
        ]
    ]

    matcher.add('valid', validation_pattern)
    #matcher.add('basic_poss', basic_poss_pattern)

    return matcher
    
