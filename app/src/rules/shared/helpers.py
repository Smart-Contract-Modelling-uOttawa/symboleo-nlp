class RuleHelpers:
    
    @staticmethod
    def is_pp(doc):
        sent = list(doc.sents)[0]
        return sent._.labels[0] == 'PP'