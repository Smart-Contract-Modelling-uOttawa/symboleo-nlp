from app.classes.spec.declaration import DeclarationProp
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.events.custom_event.noun_phrase import NounPhrase, NPTextType
from app.classes.events.custom_event.prep_phrase import PrepPhrase
from app.classes.helpers.string_to_class import CaseConverter

# TODO: E3 - Clean and break this up
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
        the_type = subject.asset_type
        if subject.is_role:
            the_value = subject.str_val
        else:
            the_value = subject.to_text(NPTextType.BASIC)
            the_value = CaseConverter.to_snake(the_value)
        
        if subject.is_role:
            the_key = f'{evt.verb.conjugations.continuous}_agent'
        else:
            if the_type == 'String':
                the_key = 'Other'
            else:
                the_key = the_type
                    
        return DeclarationProp(the_key, the_value, the_type)

    

    def map_dobject(self, dobject: NounPhrase, evt:CustomEvent) -> DeclarationProp:
        the_type = dobject.asset_type
        the_value = dobject.to_text(NPTextType.BASIC)
        the_value = CaseConverter.to_snake(the_value)

        if dobject.is_role:
            the_key = f'{evt.verb.conjugations.continuous}_target' 
        else:
            the_key = f'{evt.verb.conjugations.past}_object' 

        return DeclarationProp(the_key, the_value, the_type)
    

    def map_prep_phrase(self, prep_phrase: PrepPhrase, evt:CustomEvent) -> DeclarationProp:
        the_type = prep_phrase.pobj.asset_type
        the_value = prep_phrase.pobj.to_text() # Will prob pass in a "text_type" here (e.g. "basic")

        if prep_phrase.pobj.is_role:
            if prep_phrase.preposition == 'with':
                the_key = f'{evt.verb.conjugations.continuous}_co_agent' 
            else:
                the_key = f'{evt.verb.conjugations.continuous}_target' 
        
        else: 
            if prep_phrase.preposition == 'with':
                the_key = f'{evt.verb.lemma}_method' 
            else:
                the_key = 'Other'
        
        return DeclarationProp(the_key, the_value, the_type)
    
