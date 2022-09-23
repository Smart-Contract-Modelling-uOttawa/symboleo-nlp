dependency_match_patterns = {
    'simple': [
            {
                "RIGHT_ID": "verb",
                "RIGHT_ATTRS": {"TAG": "VBZ", "DEP": "ROOT"}
            },
            {
                "LEFT_ID": "verb",
                "REL_OP": ">",
                "RIGHT_ID": "subject",
                "RIGHT_ATTRS": {"DEP": "nsubj"}
            },
            {
                "LEFT_ID": "verb",
                "REL_OP": ">",
                "RIGHT_ID": "target",
                "RIGHT_ATTRS": {"DEP": {"IN": ["acomp", "attr"]}}
            }
        ]
}
