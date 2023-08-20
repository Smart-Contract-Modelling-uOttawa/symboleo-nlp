from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ContractEvent, ContractEventName
from app.classes.events.contract_events import ContractEvents
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

from app.src.nlp.lemmatizer import ILemmatize

class ContractActionFiller(IFillPatternUnit):
    def __init__(self, lemmatizer: ILemmatize):
        self.__lemmatizer = lemmatizer
        self.__c_dict = {
            'activate': ContractEventName.Activated,
            'terminate': ContractEventName.Terminated 
        }

    def fill(self, pattern_class: EventPatternClass, contract: SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        val = input_list[i].value

        lemma = self.__lemmatizer.lemmatize(val)
        event_name = self.__c_dict[lemma]

        result.event = ContractEvent(event_name)
        result.nl_event = ContractEvents.contract_event(event_name)
        
        return result