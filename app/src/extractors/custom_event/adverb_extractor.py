from app.classes.custom_event.adverb import Adverb, AdverbDict

class IExtractAdverb:
    def extract(self, adverb_str: str) -> Adverb:
        raise NotImplementedError()


class AdverbExtractor:
    def __init__(
        self
    ):
        self.s = 0
    
    def extract(self, adverb_str: str) -> Adverb:
        adverb_types = self._get_types(adverb_str)
     
        return Adverb(adverb_str, adverb_types)

    def _get_types(self, s: str):
        result = []
        for k in AdverbDict.adverb_type_dict:
            adv_list = AdverbDict.adverb_type_dict[k]
            if s in adv_list:
                result.append(k)

        return result


