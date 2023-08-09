import re

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.helpers.parm_checker import ParmChecker
from app.src.custom_event_extractor.element_extractor import IExtractElement

from app.src.custom_event_extractor.noun_phrase.asset_type_extractor import IExtractAssetType

# For specifically handling parameters [LIKE_THIS]
class CspNounPhraseExtractor(IExtractElement[NounPhrase]):
    def __init__(self, inner_extractor: IExtractElement[NounPhrase]):
        self.__inner_extractor = inner_extractor
        p = {}
        p['Number'] = ['amount', 'number', 'money', 'price', 'fee']
        p['Date'] = ['date', 'deadline', 'time']
        self.__parm_dict = p

    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase: 
        # Matched parm
        if ParmChecker.is_parm(str_val):
            asset_type = self._get_asset_type(str_val)
        else:
            return self.__inner_extractor.extract(str_val, contract)
        

        return NounPhrase(
            str_val, 
            head = str_val, 
            is_plural = False, 
            is_role = False, # Though it might be possible??
            det = None, 
            adjs = [],
            asset_type = asset_type,
            is_parm = True
        )


    def _get_asset_type(self, str_val:str) -> str:
        for p in self.__parm_dict:
            for pt in self.__parm_dict[p]:
                if pt in str_val.lower():
                    return p
        
        return 'String' 