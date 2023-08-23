import pickle

class NLPGetter:
    @staticmethod
    def get():
        with open('app/src/nlp/nlp.pickle', 'rb') as f:
            nlp = pickle.load(f)
        
        return nlp
    