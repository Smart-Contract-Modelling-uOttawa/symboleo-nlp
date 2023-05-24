from typing import Dict
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.custom_event.noun_phrase import NounPhrase
from app.src.extractors.value_extractor import IExtractValue

from app.src.extractors.custom_event.noun_phrase.asset_type_extractor import IExtractAssetType

class NounPhraseExtractor(IExtractValue[NounPhrase]):
    def __init__(
        self, 
        nlp,
        asset_type_extractor: IExtractAssetType
    ):
        self.__nlp = nlp
        self.__asset_type_extractor = asset_type_extractor

    # May change to full contract...
    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase:
        doc = self.__nlp(str_val)
    
        is_role = False
        asset_type = None

        # Validate
        ## Ensure that there is one noun_chunk

        # Get determiner - Might pull out and make more sophisticate
        if doc[0].tag_ == 'DT':
            det = doc[0].text
        else:
            det = None
        
        # Get the head
        heads = [x for x in doc if x.dep_ == 'ROOT']
        if len(heads) == 1:
            head = heads[0]
            is_plural = head.tag_ == 'NNS'
        else:
            raise ValueError('Invalid subject')
        
        # Get adjectives
        adjs = [x.text for x in doc 
            if x.tag_ == 'JJ' 
            or (x.dep_ == 'compound' and x.head.text == head.text)
        ]
        
        # To figure out...
        if contract:
            decls = contract.contract_spec.declarations
            is_role = self._check_role(str_val, decls)
            asset_type = self._get_asset_type(str_val, decls, head.text)
            
            if is_role:
                asset_type = 'Role'

        # Should we use is_asset again?
        return NounPhrase(
            str_val, 
            head = head.text, 
            is_plural = is_plural, 
            is_role = is_role,
            det = det, 
            adjs = adjs,
            asset_type = asset_type
        )

    def _check_role(self, str_val:str, declarations: Dict[str, Declaration]):
        if str_val in declarations:
            decl = declarations[str_val]
            return decl.base_type == 'roles'
    
        # Can probably clean this up...
        # for dk in declarations:
        #     decl = declarations[dk]
        #     if decl.base_type == 'roles':
        #         for p in declarations[dk].props:
        #             if p.key == 'name' and p.value.lower() == str_val.lower():
        #                 return True

        return False


    def _get_asset_type(self, str_val:str, declarations: Dict[str, Declaration], head_text: str):
        if str_val in declarations:
            decl = declarations[str_val]
            if decl.base_type == 'assets':
                return decl.type
        
        return self.__asset_type_extractor.extract(str_val, head_text)

