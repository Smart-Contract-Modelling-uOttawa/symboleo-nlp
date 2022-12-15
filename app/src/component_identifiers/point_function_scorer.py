from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.matcher_helper import IGetMatches

from app.classes.spec.sym_point import PointFunction, PointAtomContractEvent, ContractEvent

from app.classes.spec.helpers import TimeUnitStr

class PointFunctionScorer(IScorePrimitives):
    def __init__(
        self,
        matcher: IGetMatches,
        tvi_scorer: IScorePrimitives,
        tus_scorer: IScorePrimitives
    ):
        self.__matcher = matcher
        self.__tus_scorer = tus_scorer
        self.__tvi_scorer = tvi_scorer
        ## Need a point identifier as well
        
    def score(self, req: ContractUpdateRequest) -> ScoredPrimitive:
        # Look for tvi and tus
        # If those are both there, then look for 
        tus = self.__tus_scorer.score(req)

        tvi = self.__tvi_scorer.score(req)

        if not tus or not tvi:
            return None
        
        # Can look for a point here...
        # Can also default back to an anchor point maybe
        default_point = PointAtomContractEvent(ContractEvent('activated'))

        prim = PointFunction(default_point, tvi.obj, tus.obj)
        score = tvi.score * tus.score

        return ScoredPrimitive(prim, score)




    ## Can hopefully get rid of all this... depends on testing performance 
    ## Assumption: Only taking the first time unit that is found...
    ## this is not a great assumption to make... e.g. "between 2 and 4 days" would be a problem
    def identify_old(self, doc) -> ScoredPrimitive:
        
        trigger_words = [x for x in doc if self._in_unit_list(x)]

        datetime_ents = [x for x in trigger_words if self._is_datetime_entity(x)]

        if len(datetime_ents) > 0:
            primitive_text = self._pluralize(datetime_ents[0].text)
            score = 1
        elif len(trigger_words) > 0:
            primitive_text = self._pluralize(trigger_words[0].text)
            score = 0.5
        else:
            primitive_text = ''
            score = 0
        
        return ScoredPrimitive(TimeUnitStr(primitive_text), score)


    def _in_unit_list(self, x): return x.text.lower() in self.__all_units

    def _is_datetime_entity(self, x): return x.ent_type_ in ['TIME', 'DATE']
    
    def _pluralize(self, x):
        for k in self.__dict:
            if x in self.__dict[k]:
                return k
        
        return ''
    
