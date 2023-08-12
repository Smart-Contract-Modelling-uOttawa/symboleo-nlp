from app.classes.spec.symboleo_contract import SymboleoContract
import re

from app.src.custom_event_extractor.nlp.label_getter import IGetLabels

class IExtractAssetType:
    def extract(self, str_val: str, head: str, contract: SymboleoContract) -> str:
        raise NotImplementedError()

class AssetTypeExtractor(IExtractAssetType):
    def __init__(self, label_getter: IGetLabels) -> None:
        self.__label_getter = label_getter
        
        d = {}
        d['FAC'] = 'Location'
        d['DATE'] = 'Date'
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
    def extract(self, str_val: str, head: str, contract: SymboleoContract) -> str:
        # Check for role or asset
        decls = contract.contract_spec.declarations
        if str_val in decls:
            decl = decls[str_val]
            if decl.base_type == 'roles':
                return 'Role'
            elif decl.base_type == 'assets':
                return decl.type
        
        # # Check enums
        # for x in contract.domain_model.enums:
        #     if str_val.lower() in [x.lower() for x in x.enum_items]:
        #         return x.name

        # Money Amount
        money = re.search('\$\d+(?:\.\d+)?', str_val)
        if money:
            return 'Money'
        
        # Check custom dict
        if str_val in self.__str_dict:
            return self.__str_dict[str_val]
        
        # Check labels
        label = self.__label_getter.get(str_val)
        if label and label in self.__ent_dict:
            return self.__ent_dict[label]
        
        # Default value
        return head.capitalize()
    