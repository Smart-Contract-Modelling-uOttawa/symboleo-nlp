from spacy.matcher import Matcher
import copy
from typing import Dict
from app.src.rules.domain_model.location.coref_getter import IGetCorefs
from app.classes.contract_update_request import ContractUpdateRequest

class IBuildRoleScores:
    def build(self, req: ContractUpdateRequest):
        raise NotImplementedError()


class RoleScoreBuilder(IBuildRoleScores):
    def __init__(
        self,
        nlp,
        init_scores: Dict[str, float],
        coref_getter: IGetCorefs
    ):
        self.__nlp = nlp
        self.__init_scores = init_scores
        self.__coref_getter = coref_getter
    
    
    def build(self, req: ContractUpdateRequest):
        doc = req.doc
        role_score_dict = copy.deepcopy(self.__init_scores)

        ## Role matches
        role_matcher = Matcher(self.__nlp.vocab)
        for role_name in role_score_dict:
            role_pattern = [
                [{ "POS": "NOUN", "LOWER": role_name }]
            ]
            role_matcher.add(role_name, role_pattern) 
        role_matches = role_matcher(doc)

        # Corefs 
        ## Need to improve the template_string
        template_string = self._get_template_string(req)
        coref_set = self.__coref_getter.get(doc, req.key, template_string)

        # Look through role matches
        # Find the role_match (e.g. buyer/seller)
        for m_id, start, end in role_matches:
            s_id = self.__nlp.vocab.strings[m_id]
            if s_id in role_score_dict:
                role_score_dict[s_id] = 1
        
        # Look through corefs
        for cr in coref_set:
            corefs = coref_set[cr]
            for c in corefs:
                if c in role_score_dict:
                    role_score_dict[c] = 1
        
        return role_score_dict
    
    def _get_template_string(self, req: ContractUpdateRequest) -> str:
        for nk in req.contract.template_strings['obligations']:
            sent = req.contract.template_strings['obligations'][nk]
            if req.key in sent:
                return sent
        
        raise ValueError(f'Invalid key... {req.key}')