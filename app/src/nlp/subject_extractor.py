from app.classes.other.subject import Subject

class IExtractSubject:
    def extract(self, subj_str: str) -> Subject:
        raise NotImplementedError()


class SubjectExtractor:    
    def __init__(self, nlp):
        self.__nlp = nlp

    def extract(self, subj_str: str) -> Subject:
        doc = self.__nlp(subj_str)

        # Validate
        ## Ensure that there is one noun_chunk and it is equal

        # Get determiner
        if doc[0].tag_ == 'DT':
            det = doc[0].text
        else:
            det = None
        
        # Get adjectives
        adjs = [x.text for x in doc if x.tag_ == 'JJ']
        
        # Get the head
        heads = [x for x in doc if x.dep_ == 'ROOT']
        if len(heads) == 1:
            head = heads[0]
            is_plural = head.tag_ == 'NNS'
        else:
            raise ValueError('Invalid subject')
    
        return Subject(subj_str, head.text, is_plural, det, adjs)
