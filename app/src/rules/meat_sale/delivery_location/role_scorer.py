from typing import List, Tuple
from app.classes.domain_model.domain_model import DomainProp
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.meat_sale.delivery_location.role_score_builder import IBuildRoleScores

class RoleScorer(IScoreStuff):
    def __init__(
        self, 
        nlp,
        role_score_builder: IBuildRoleScores
    ):
        self.__nlp = nlp
        self.__role_score_builder = role_score_builder
    
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        results = []
        doc = req.doc
        domain_model = req.contract.domain_model

        # First build an updated role score dict based on keywords and coref
        role_score_dict = self.__role_score_builder.build(req)
    
        pieces = list(doc.noun_chunks) # Will be more sophisticated... addresses, noun_chunks, etc
        ## Want to treat addresses differently - requires an exact match...

        for role in role_score_dict:
            role_score = role_score_dict[role]
            role_props = domain_model.roles[role].props

            for p in pieces:
                print('piece', p)
                # Have a better scoring mechanism
                p_score_dict = self._sim_prop_check(role_props, p)

                for ps in p_score_dict:
                    next_score = p_score_dict[ps] * role_score
                    results.append((f'{role}.{ps}', next_score))
        
        return results
    

    def _sim_prop_check(self, props: list[DomainProp], text: str):
        result = {}

        for x in props:
            dk = self.__nlp(x.key)
            sk = dk.similarity(text)

            dv = self.__nlp(x.value)
            sv = dv.similarity(text)

            result[x.key] = sk*sv
        
        return result