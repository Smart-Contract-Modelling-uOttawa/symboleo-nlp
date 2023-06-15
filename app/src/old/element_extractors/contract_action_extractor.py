
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ContractEventName
from app.src.element_extractors.element_extractor import IExtractElement
from app.src.element_extractors.verb.lemmatizer import ILemmatize
from app.classes.events.template_event.contract_components import ContractVerbs

class ContractActionExtractor(IExtractElement[ContractEventName]):    
    def __init__(self, lemmatizer: ILemmatize):
        self.__lemmatizer = lemmatizer
    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> ContractEventName:
        lemma = self.__lemmatizer.lemmatize(str_val)

        # Then have a dict to look it up, based on the lemma
        result = ContractVerbs.contract_verb_dict[lemma]

        return result
