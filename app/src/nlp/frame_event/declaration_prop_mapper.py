from typing import List
from app.classes.spec.domain_object import Asset
from app.src.nlp.frame_event.domain_keys import DomainKeys
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.other.frame_event import FrameEvent
from app.classes.other.noun_phrase import NounPhrase
from app.classes.other.noun_phrase import NounPhrase
from app.classes.other.prep_phrase import PrepPhrase

from app.src.nlp.frame_event.asset_type_extractor import IExtractAssetType

# I think we should be passing in ALL assets: both existing from contract and the new ones...
# Dont need declarations at this point
# Should also be passing in the whole frame event..
class IMapDeclarationProps:
    def map_subject(self, subject: NounPhrase, evt:FrameEvent, asset_decls: List[Asset] = None) -> DeclarationProp:
        raise NotImplementedError()

    def map_dobject(self, dobject: NounPhrase, evt:FrameEvent, asset_decls: List[Declaration] = None) -> DeclarationProp:
        raise NotImplementedError()
    
    def map_prep_phrase(self, prep_phrase: PrepPhrase, evt:FrameEvent, asset_decls: List[Declaration] = None) -> DeclarationProp:
        raise NotImplementedError()
    
# Can split this up further: separate for key, type, etc
class DeclarationPropMapper(IMapDeclarationProps):
    def __init__(self, asset_type_extractor: IExtractAssetType):
        self.__asset_type_extractor = asset_type_extractor
        # framenet
        # Other nlp...

    # Also depends on what else is used
    ## e.g. we only want ONE agent
    ## I may also use the verb
    ### e.g. if verb is "allow", then subject could be "allowing_agent"... dobj could be "obj_to_allow/allowing_target"... May be easy..
    def map_subject(self, subject: NounPhrase, evt: FrameEvent, asset_decls: List[Declaration] = None) -> DeclarationProp:
        the_type = self._get_type(subject, asset_decls)
        the_value = subject.to_text() # Will prob pass in a "text_type" here (e.g. "basic")
        
        # Key (Hard part!): use framenet, verb, role, asset
        # Not sure the asset_type will be used twice
        ## In some cases, the key may just be lower-cased
        ## For example, "buyer pays $100"... 
        ### key=payer, value=buyer, type=Role
        ### key=amount, value=$100, type=Amount
        the_key = '' 
        if subject.is_role:
            the_key = f'{evt.verb.conjugations.continuous}_agent'
        else:
            if the_type == 'String':
                the_key = DomainKeys.OTHER.value
            else:
                the_key = the_type.lower()
                    
        return DeclarationProp(the_key, the_value, the_type)

    

    def map_dobject(self, dobject: NounPhrase, evt:FrameEvent, asset_decls: List[Declaration] = None) -> DeclarationProp:
        the_type = self._get_type(dobject, asset_decls)
        the_value = dobject.to_text() # Will prob pass in a "text_type" here (e.g. "basic")

        if dobject.is_role:
            the_key = f'{evt.verb.conjugations.continuous}_target' 
        else:
            the_key = f'{evt.verb.lemma}_object' 


        return DeclarationProp(the_key, the_value, the_type)
    

    def map_prep_phrase(self, prep_phrase: PrepPhrase, evt:FrameEvent, asset_decls: List[Declaration] = None) -> DeclarationProp:
        the_type = self._get_type(prep_phrase.pobj, asset_decls)
        the_value = prep_phrase.pobj.to_text() # Will prob pass in a "text_type" here (e.g. "basic")

        the_key = ''
        if prep_phrase.pobj.is_role:
            the_key = f'{evt.verb.conjugations.continuous}_target' 
        elif prep_phrase.preposition == 'with':
            the_key = f'{evt.verb.lemma}_method' 
        else:
            the_key = DomainKeys.OTHER.value
        
        return DeclarationProp(the_key, the_value, the_type)
    

    # Pull this out
    def  _get_type(self, np: NounPhrase, assets: List[Asset]):
        if np.is_role:
            return 'Role'
        else:
            return self.__asset_type_extractor.extract(np)
