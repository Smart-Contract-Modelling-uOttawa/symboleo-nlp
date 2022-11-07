# Should be able to generalize this
class DtfpTest:
    template = None
    sentence = None
    expected_sym = None

    def __init__(self, sentence, expected_sym):
        self.sentence = sentence
        self.expected_sym = expected_sym

test_suite = [
    DtfpTest(
        'within two months',
        'WhappensBefore(delivered, Date.add(activated(self), two, months))'
    ),
    DtfpTest(
        'before April 25, 2022',
        'WhappensBefore(delivered, April 25, 2022)'
    )
]