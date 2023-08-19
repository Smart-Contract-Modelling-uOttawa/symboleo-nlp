from app.classes.spec.symboleo_contract import SymboleoContract
import re

from app.src.nlp.label_getter import IGetLabels

class AssetType:
    def __init__(self, type_name:str, id:str = ''):
        self.type_name = type_name
        self.id = id

class IExtractAssetType:
    def extract(self, str_val: str, head: str, contract: SymboleoContract) -> AssetType:
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
        s['contract'] = 'Contract'
        s['agreement'] = 'Contract'
        self.__str_dict = s

    # Will have a barrage of different potential extractors here 
    def extract(self, str_val: str, head: str, contract: SymboleoContract) -> AssetType:
        # Check for role or asset (by NAME, not id)
        decls = {x.name: x for x in contract.contract_spec.declarations.values()}

        if str_val in decls:
            decl = decls[str_val]
            if decl.base_type == 'roles':
                return AssetType('Role', decl.id)
            elif decl.base_type == 'assets':
                return AssetType(decl.type, decl.id)
        
        # # Check enums
        # for x in contract.domain_model.enums:
        #     if str_val.lower() in [x.lower() for x in x.enum_items]:
        #         return x.name

        # Money Amount
        money = re.search('\$\d+(?:\.\d+)?', str_val)
        if money:
            return AssetType('Money')
        
        # Check custom dict
        if str_val in self.__str_dict:
            return AssetType(self.__str_dict[str_val])
            
        # Check labels
        label = self.__label_getter.get(str_val)
        if label and label in self.__ent_dict:
            return AssetType(self.__ent_dict[label])
        
        # Default value
        return AssetType(head.capitalize())
    