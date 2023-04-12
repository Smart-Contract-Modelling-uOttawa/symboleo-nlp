class Statement:
    def __init__(self, subj, verb, pred):
        self.subj = subj
        self.verb = verb
        self.pred = pred
    
    def __eq__(self, other):
        return self.subj == other.subj and self.verb == other.verb and self.pred == other.pred


class IExtractStatements:
    def extract(self, s:str)-> Statement:
        raise NotImplementedError()


class StatementExtractor(IExtractStatements):
    def __init__(self, nlp):
        self.__nlp = nlp
        linking_lemmas = ['be', 'become', 'seem']
        sense_lemmas = ['look', 'appear', 'sound', 'taste', 'smell', 'feel']
        self.__lemma_list = linking_lemmas + sense_lemmas
    
    # Question: Should I keep articles (a, the, ...)
    def extract(self, s: str) -> Statement:
        doc = self.__nlp(s)
        sent = list(doc.sents)[0]
        cs = list(sent._.children)

        if cs[0]._.labels[0] == 'NP':
            np = cs[0]

            if cs[1]._.labels[0] == 'VP':
                cs2 = list(cs[1]._.children)
                verb = cs2[0][0]

                if verb.pos_ in ['VERB', 'AUX']:
                    if verb.lemma_ in self.__lemma_list:
                        
                        pred = cs2[1]
                
                        pred_labels = list(pred._.labels)
                        if len(pred_labels) > 0:
                            if pred_labels[0] in ['ADJP', 'NP']:
                                return Statement(np.text, verb.text, pred.text)
                            
        raise ValueError('Invalid statement entered')
            