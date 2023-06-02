from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.adverb import Adverb, AdverbDict
from app.src.selection.element_extractors.value_extractor import IExtractValue

class AdverbExtractor(IExtractValue[Adverb]):
    def __init__(
        self
    ):
        self.s = 0
    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> Adverb:
        adverb_types = self._get_types(str_val)
     
        return Adverb(str_val, adverb_types)


    def _get_types(self, s: str):
        result = []
        for k in AdverbDict.adverb_type_dict:
            adv_list = AdverbDict.adverb_type_dict[k]
            if s in adv_list:
                result.append(k)

        return result


