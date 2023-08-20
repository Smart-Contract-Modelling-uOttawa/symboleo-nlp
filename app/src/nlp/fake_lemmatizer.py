from app.src.nlp.lemmatizer import ILemmatize

class FakeLemmatizer(ILemmatize):
    def __init__(self):
        self.__dict = {
            'become': 'become',
            'becomes': 'become',
            'provides': 'provide',
            'abandons': 'abandon',
            'occupies': 'occupy',
            'allows': 'allow',
            'receiving': 'receive',
            'authorizes': 'authorize',
            'completes': 'complete',
            'starts': 'start',
            
            'activate': 'activate',
            'activated': 'activate',
            'activates': 'activate',
            'activating': 'activate',

            'terminate': 'terminate',
            'terminated': 'terminate',
            'terminates': 'terminate',
            'terminating': 'terminate',
            
            'beginning': 'begin',
            'begins': 'begin',
            'disrupts': 'disrupt',
            'sending': 'send',
            'occupying': 'occupy',
            'returns': 'return',
            'submits': 'submit',
            'happening': 'happen',
            'completes': 'complete',
            'misses': 'miss',
            'mandates': 'mandate',
            'pays': 'pay',
            'delivers': 'deliver',
            'breaches': 'breach'
        }
    
    def get_dict(self):
        return self.__dict

    def lemmatize(self, s: str) -> str:
        if s in self.__dict:
            return self.__dict[s]
        else:
            print(f'{s} not found in fake lemmatizer...')
            return s
