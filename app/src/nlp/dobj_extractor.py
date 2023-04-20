from app.classes.other.dobject import DObject

class IExtractDobject:
    def extract(self, dobj_str: str) -> DObject:
        raise NotImplementedError()


class DobjectExtractor(IExtractDobject):    
    def __init__(self, nlp):
        self.__nlp = nlp

    def extract(self, dobj_str: str) -> DObject:
        doc = self.__nlp(dobj_str)

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
    
        return DObject(dobj_str, head.text, is_plural, det, adjs)
