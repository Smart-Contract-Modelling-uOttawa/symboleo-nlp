from typing import Dict
from spacy.matcher import Matcher
from app.classes.symboleo_contract import DomainModel
from app.classes.domain_model.domain_model import DomainProp

class IExtractLocation:
    def extract(self, value: str, domain_model: DomainModel) -> str:
        raise NotImplementedError()


class LocationExtractor(IExtractLocation):
    def __init__(
        self,
        nlp,
        matcher: Matcher
    ):
        self.__nlp = nlp
        self.__matcher = matcher
        self.__default_value = 'buyer'

    
    def extract(self, value: str, domain_model: DomainModel) -> str:
        doc = self.__nlp(value)

        matches = self.__matcher(doc)

        # Use matcher for validation
        self._validate_pattern(matches)

        # Set the default
        noun_chunks = list(doc.noun_chunks)
        result = self._get_default(noun_chunks)

        # Extract entities: Noun chunks, addresses, roles, etc
        addresses = [] # extract address (use another matcher)
        ## May have more than just addresses...

        # Instead of threshold, could have a scoring system
        # Can generalize this - since we have collections of entities (addresses, noun_chunks)
        # Each collection of entities is being compared against the domain prop
        # Can pull out the domain prop extraction - which is one of the key pieces here, and generalize
        target_roles = self._get_target_roles(domain_model, doc)
        threshold = 0.25

        for role in target_roles:
            print('ROLE', role)
            role_score = target_roles[role]
            role_props = domain_model.roles[role].props

            for ad in addresses:
                print('ADDRESS', ad)
                ad_res = self._sim_prop_check(role_props, ad, threshold, role_score)
                if ad_res:
                    result = f'{role}.{ad_res}'
                
            for nc in noun_chunks:
                print('NC', nc)
                nc_res = self._sim_prop_check(role_props, nc, threshold, role_score)
                if nc_res:
                    result = f'{role}.{nc_res}'

        return result
    

    def _sim_prop_check(self, props: list[DomainProp], text: str, threshold, init_score):
        for x in props:
            dk = self.__nlp(x.key)
            sk = dk.similarity(text)

            dv = self.__nlp(x.value)
            sv = dv.similarity(text)
            
            score = sv*sk*init_score
            print(x.to_sym(), score)
            
            if score > threshold:
                print('MATCH!')
                return x.key

        return None


    def _get_target_roles(self, domain_model: DomainModel, doc) -> Dict[str, float]:
        result = {}

        # Start with the roles from the domain model
        # May want to even pass a pre-set dict in to this. E.g. may want "buyer" to have a default advantge on this
        all_roles = list(domain_model.roles.keys())

        # Or may be better to just pass the matches into here and sort it out...
        role_matcher = Matcher(self.__nlp.vocab)
        role_pattern = [
            [{ "POS": "NOUN", "LOWER": { "IN": all_roles } }]
        ]
        matches = [] # Should also include coref on possessive pronouns

        # If the text is directly in there
        for role in all_roles:
            result[role] = 0.5
            if role in matches:
                result[role] = 1

        return result


    def _validate_pattern(self, matches):
        basic_match = [m for m in matches if self.__nlp.vocab.strings[m[0]] == 'basic'] 

        if len(basic_match) != 1: # Can add better validation here
            raise 'Value does not match expected pattern'
        
        return
    

    def _get_default(self, noun_chunks):
        if len(noun_chunks) > 0:
            return noun_chunks[0].text
        else:
            return self.__default_value

