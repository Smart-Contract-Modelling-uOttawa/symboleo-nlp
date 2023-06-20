from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.custom_event import CustomEvent, Verb, NounPhrase, Adverb, Predicate, PrepPhrase
from app.classes.operations.user_input import UserInput, UnitType

from app.src.element_extractors.element_extractor import IExtractElement 

class IExtractCustomEvents:
    def extract(self, input_list: List[UserInput], contract: SymboleoContract) -> CustomEvent:
        raise NotImplementedError()
    
class CustomEventExtractor(IExtractCustomEvents):
    def __init__(
        self,
        verb_extractor: IExtractElement[Verb],
        np_extractor: IExtractElement[NounPhrase],
        advb_extractor: IExtractElement[Adverb],
        pred_extractor: IExtractElement[Predicate],
        pp_extractor: IExtractElement[PrepPhrase]
    ):
        self.__verb_extractor = verb_extractor
        self.__np_extractor = np_extractor
        self.__advb_extractor = advb_extractor
        self.__pred_extractor = pred_extractor
        self.__pp_extractor = pp_extractor

    def extract(self, input_list: List[UserInput], contract: SymboleoContract) -> CustomEvent:
        unit_type_list = [x.unit_type for x in input_list]
        
        if UnitType.CUSTOM_EVENT in unit_type_list:
            subj_str = [x.value for x in input_list if x.unit_type == UnitType.SUBJECT][0]
            subj = self.__np_extractor.extract(subj_str, contract)


            verb_str = [x.value for x in input_list if x.unit_type in [UnitType.LINKING_VERB, UnitType.TRANSITIVE_VERB, UnitType.INTRANSITIVE_VERB]][0]
            verb = self.__verb_extractor.extract(verb_str, contract)

            dobj = None
            dobj_strs = [x.value for x in input_list if x.unit_type == UnitType.DOBJ]
            
            if dobj_strs:
                dobj = self.__np_extractor.extract(dobj_strs[0], contract)
                print(dobj.to_text())
            
            pred = None
            pred_strs = [x.value for x in input_list if x.unit_type == UnitType.PREDICATE]
            if pred_strs:
                pred = self.__pred_extractor.extract(pred_strs[0], contract)
            
            advb = None
            advb_strs = [x.value for x in input_list if x.unit_type == UnitType.ADVERB]
            if advb_strs:
                advb = self.__advb_extractor.extract(advb_strs[0], contract)
            
            pps = []
            for pp_str in [x.value for x in input_list if x.unit_type == UnitType.PREP_PHRASE]:
                pp = self.__pp_extractor.extract(pp_str, contract)
                pps.append(pp)
            
            negation = False
            if [x.value for x in input_list if x.unit_type == UnitType.FAILS_TO]:
                negation = True

            return CustomEvent(
                subj,
                verb,
                advb,
                dobj,
                pred,
                pps,
                negation
            )
        
        return None
            
