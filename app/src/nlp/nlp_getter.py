import pickle

class NLPGetter:
    FILEPATH = 'app/src/nlp'
    FILENAME = 'nlp' 
    @staticmethod
    def get():
        with open(f'./{NLPGetter.FILEPATH}/{NLPGetter.FILENAME}.pickle', 'rb') as f:
            nlp = pickle.load(f)
        
        return nlp
    