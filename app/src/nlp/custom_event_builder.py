import random
import copy
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.domain_object import DomainEvent, Asset, DomainObject, DomainProp
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel

from app.src.nlp.verb_creator import ICreateVerbs, Verb, VerbType

# Will remove this. But keep it for now to transfer code over 

class IBuildCustomEvent:
    def build(self):
        raise NotImplementedError()

# This should create a new event
## Includes the NL and anything that goes on the Domain Model (assets, events, etc). and a declaration
## Might need a "false" domain model - we copy it, then it gets updated as needed. Then at the end we re-add it to the contract (replace)
## Makes it transactional
## Will likely pull out the input() into an interface...
class CustomEventBuilder:
    def __init__(
            self,
            contract: SymboleoContract, 
            verb_creator: ICreateVerbs
        ):
        self.__contract = contract
        self.__verb_creator = verb_creator


    def build(self):
        # May have a separate EventNL object that gets constructed here instead
        ## Similar to how the Selection object is constructed...
        new_dm = copy.deepcopy(self.__contract.domain_model)
        arr = []
        dm_props = []
        decl_props = []
        accessories = []

        # Option for negation?

        subj = self._get_subject(new_dm)
        arr.append(subj.name)
        dm_props.append(DomainProp('subject', 'String')) # Will need to choose the right key
        decl_props.append(DeclarationProp('subject', subj.name, 'String'))
    
        verb = self._get_verb()
        arr.append(verb.verb_str)
        vt = verb.verb_type

        if vt == VerbType.INTRANSITIVE:
            adverb = self._get_adverb(verb)
            arr.append(adverb)
        
        else:
            if vt == VerbType.LINKING:
                pred = self._get_predicate()
                arr.append(pred)

            elif vt == VerbType.TRANSITIVE:
                dobj = self._get_dobj() # Will also want to use roles and assets
                arr.append(dobj)
                dm_props.append(DomainProp('object', 'String')) # Will need to choose the right key
                decl_props.append(DeclarationProp('object', dobj, 'String'))

        
            adverb = self._get_adverb(verb)
            arr.append(adverb)

        adjuncts = self._get_adjuncts() # Also use roles and assets
        for i, (prep, pobj) in enumerate(adjuncts):
            arr.append(f'{prep} {pobj}')
            dm_props.append(DomainProp(f'prop_{i+1}', 'String')) # Will need to choose the right key
            decl_props.append(DeclarationProp(f'prop_{i+1}', pobj, 'String'))
            

        result_str = ' '.join(arr)
        print(f'STR: {result_str}')

        # Will likely have separate mapping functions
        domain_event_name = f'{verb.verb_str.title()}{adverb.title()}' # PascalCase: VerbAdverb ?
        domain_event = DomainEvent(domain_event_name, dm_props, 'XXX')
        
        declaration_name = f'evt_{domain_event_name}'
        declaration = Declaration(declaration_name, 'events', domain_event_name, decl_props, result_str)
        # Handle accessories...

        # Return a more complex object
        return (
            domain_event,
            declaration,
            accessories
        )
    

    # Result is a domain asset or role
    def _get_subject(self, domain_model: DomainModel) -> DomainObject:
        # Roles and assets; or custom
        roles = domain_model.roles
        assets = domain_model.assets

        for rk in roles:
            print(f'- Role: {rk}')
        
        for ak in assets:
            print(f'- Asset: {ak}')
        
        # Choose existing subject or add custom
        user_input = input('Subject: ')

        if user_input in roles:
            result = roles[user_input]
        
        elif user_input in assets:
            result = assets[user_input]
        
        else:
            # Create new asset
            ## What about props? or basetype...?
            result = Asset(user_input, [])
        
        # Should I add it to the domain model?

        return result



    def _get_verb(self) -> Verb:
        user_input = input('Verb: ')
        result = self.__verb_creator.create(user_input)
        return result


    def _get_dobj(self):
        result = input('Direct object: ')
        return result


    def _get_predicate(self, verb):
        # May use verb to get some suggestions...
        result = input('Predicate: ')
        return result


    def _get_adverb(self, verb: Verb):
        result = input('Adverb (optional): ')
        # Validation... likely pull this out
        return result
    
    # Needs a custom object. For now its a tuple (prep, pobj)
    def _get_adjuncts(self):
        results = []
        trigger = True
        while trigger:
            prep = self._select_preposition()
            if not prep:
                break
            pobj = self._get_pobj(prep)
            results.append((prep, pobj))
        return results
    

    def _select_preposition(self):
        result = input('Select Preposition (or blank to quit): ')
        # to, with, for, ...
        return result


    def _get_pobj(self, prep: str):
        result = input('Prepositional object: ')
        return result

