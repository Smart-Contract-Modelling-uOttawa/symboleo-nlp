from app.src.custom_event_extractor.verb.lemmatizer import ILemmatize

class FakeLemmatizer(ILemmatize):
    def __init__(self):
        self.__dict = {
            'become': 'become',
            'provides': 'provide',
            'abandons': 'abandon',
            'occupies': 'occupy',
            'allows': 'allow',
            'receiving': 'receive',
            'authorizes': 'authorize',
            'completes': 'complete',
            'starts': 'start',
            'terminates': 'terminate',
            'terminating': 'terminate',
            'beginning': 'begin',
            'begins': 'begin',
            'disrupts': 'disrupt',
            'sending': 'send',
            'occupying': 'occupy',
        }

    def lemmatize(self, s: str) -> str:
        if s in self.__dict:
            return self.__dict[s]
        else:
            print(f'{s} not found in fake lemmatizer...')
            return s
