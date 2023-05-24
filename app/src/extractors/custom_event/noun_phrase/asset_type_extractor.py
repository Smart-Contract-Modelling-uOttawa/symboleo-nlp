import re

class IExtractAssetType:
    def extract(self, str_val: str, head:str) -> str:
        raise NotImplementedError()

class AssetTypeExtractor(IExtractAssetType):
    def __init__(self, nlp) -> None:
        self.__nlp = nlp
        # wordnet, framenet, regex...
        
        d = {}
        d['FAC'] = 'Location'
        d['GPE'] = 'Location'
        d['ORG'] = 'Org'
        d['PRODUCT'] = 'Product'
        d['EVENT'] = 'MajorEvent'
        d['LANGUAGE'] = 'Language'
        d['MONEY'] = 'Money'
        self.__ent_dict = d

        s = {}
        s['credit card'] = 'PaymentMethod'
        s['cash'] = 'PaymentMethod'
        self.__str_dict = s

    # Will have a barrage of different potential extractors here 
    def extract(self, str_val: str, head:str) -> str:
        # Money Amount
        money = re.search('\$\d+(?:\.\d+)?', str_val)
        if money:
            return 'Money'
        
        # Check custom dict
        if str_val in self.__str_dict:
            return self.__str_dict[str_val]
        
        # Check spacy entities
        doc = self.__nlp(str_val)
        if len(doc.ents) > 0:
            label = doc.ents[0].label_
            if label in self.__ent_dict:
                return self.__ent_dict[label]
        
        # Default value
        return head.capitalize()
        #return 'Other'
    