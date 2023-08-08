from app.classes.spec.declaration import DeclarationProp
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.events.custom_event.noun_phrase import NounPhrase, NPTextType
from app.classes.events.custom_event.prep_phrase import PrepPhrase
from app.classes.helpers.string_to_class import CaseConverter

# Given a noun phrase and its CustomEvent context, map it to a declaration property
## Requires a key, a value, and a type
## The key should be somewhat descriptive. It will be used by the domain model object
### Identify if its a agent or some other property
## The type will be the asset type of the incoming noun phrase
## The value will be some form of the to_text() function on the incoming noun phrase
# Note: These are all based on rough heuristics, and could be replaced by more evidence-based models
class IMapDeclarationProps:
    def map_subject(self, subject: NounPhrase, evt:CustomEvent) -> DeclarationProp:
        raise NotImplementedError()

    def map_dobject(self, dobject: NounPhrase, evt:CustomEvent) -> DeclarationProp:
        raise NotImplementedError()
    
    def map_prep_phrase(self, prep_phrase: PrepPhrase, evt:CustomEvent) -> DeclarationProp:
        raise NotImplementedError()
    
class DeclarationPropMapper(IMapDeclarationProps):
    def __init__(self):
        self.s = 0
        # framenet
        # Other nlp...?

    def map_subject(self, subject: NounPhrase, evt: CustomEvent) -> DeclarationProp:
        asset_type = subject.asset_type

        if subject.is_role:
            the_key = f'{evt.verb.conjugations.continuous}_agent'
            the_value = subject.to_text()
        else:
            the_key = f'{evt.verb.conjugations.continuous}_subject'
            the_value = CaseConverter.to_snake(subject.to_text(NPTextType.BASIC))
                    
        return DeclarationProp(the_key, the_value, asset_type)

    
    def map_dobject(self, dobject: NounPhrase, evt:CustomEvent) -> DeclarationProp:
        asset_type = dobject.asset_type
        the_value = CaseConverter.to_snake(dobject.to_text(NPTextType.BASIC))

        if dobject.is_role:
            the_key = f'{evt.verb.conjugations.past}_target' 
        else:
            the_key = f'{evt.verb.conjugations.past}_object' 
        
        if dobject.is_parm:
            the_key = dobject.str_val[1:-1].lower()
            the_value = dobject.str_val

        return DeclarationProp(the_key, the_value, asset_type)
    

    def map_prep_phrase(self, prep_phrase: PrepPhrase, evt:CustomEvent) -> DeclarationProp:
        asset_type = prep_phrase.pobj.asset_type
        the_value = prep_phrase.pobj.to_text() # Will prob pass in a "text_type" here (e.g. "basic")

        if prep_phrase.pobj.is_role:
            if prep_phrase.preposition == 'with':
                the_key = f'{evt.verb.conjugations.continuous}_co_agent' 
            else:
                the_key = f'{evt.verb.conjugations.continuous}_target' 
        
        else: 
            if prep_phrase.preposition == 'with':
                the_key = f'{evt.verb.lemma}_method' 
            elif prep_phrase.preposition == 'for':
                the_key = f'{evt.verb.lemma}_detail'
            else:
                the_key = f'{evt.verb.lemma}_detail'
        
        return DeclarationProp(the_key, the_value, asset_type)
    
