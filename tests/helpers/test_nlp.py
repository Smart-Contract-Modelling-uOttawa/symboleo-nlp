import pickle

class TestNLP:

    @staticmethod
    def get_nlp():
        
        # If not there, then will need to create it...
        with open('nlp/nlp.pickle', 'rb') as f:
            nlp = pickle.load(f)
        
        return nlp