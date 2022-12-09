import re
from typing import Tuple
from spacy.tokens.doc import Doc
from app.classes.contract_update_request import ContractUpdateRequest

class IPrepCorefTemplates:
    def prep(self, req: ContractUpdateRequest) -> Tuple[Doc, int]:
        raise NotImplementedError()


class CorefTemplatePrepper(IPrepCorefTemplates):
    def __init__(self, nlp):
        self.__nlp = nlp
    
    def prep(self, req: ContractUpdateRequest) -> Tuple[Doc, int]:
        template_string = self._get_template_string(req)

        # replace any other keys (not counting target) with blanks
        t_string = template_string.replace(f'[{req.key}]', f'{req.doc.text}')
        t_string = re.sub(r"\[.+?\]", '', t_string)
        t_string = re.sub(r"  ", ' ', t_string)

        upto_ind = t_string.index(f'{req.doc.text}')
        upto_str = t_string[:upto_ind]
        upto_doc = self.__nlp(upto_str)

        base_ind = len(upto_doc)

        full_doc = self.__nlp(t_string)

        return full_doc, base_ind

    

    def _get_template_string(self, req: ContractUpdateRequest) -> str:
        for nk in req.contract.template_strings['obligations']:
            sent = req.contract.template_strings['obligations'][nk]
            if req.key in sent:
                return sent
        
        for nk in req.contract.template_strings['powers']:
            sent = req.contract.template_strings['powers'][nk]
            if req.key in sent:
                return sent
        
        raise ValueError(f'Invalid key... {req.key}')
