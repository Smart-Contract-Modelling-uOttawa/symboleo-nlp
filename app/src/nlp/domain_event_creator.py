import copy
from typing import Dict, List
from app.classes.symboleo_contract import DomainModel
from app.classes.spec.domain_model import DomainProp, DomainEvent

import nltk
from nltk.corpus.reader.framenet import FramenetCorpusReader, AttrDict, PrettyDict

from app.src.nlp.standard_events import standard_event_dict
# May need a wrapper for framenet

# TODO: Will need to split this all up and clean up the framenet stuff
class ICreateDomainEvents:
    def create(self) -> DomainEvent:
        raise NotImplementedError()
    
class DomainEventCreator(ICreateDomainEvents):
    def __init__(self, fn: FramenetCorpusReader, domain_model: DomainModel):
        #nltk.download('framenet_v17')
        self.__dm = domain_model
        self.__prop_types = list(domain_model.assets.keys()) + list(domain_model.roles.keys()) + ['String', 'Number', 'Date', 'Role', 'Asset']
        self.__fn = fn

    def create(self) -> DomainEvent:
        print('Creating a new event.')
        print('1 - Choose from standard contract events')
        print('2 - Create a custom event')

        user_k = int(input('Select #: '))

        if user_k == 1:
            return self.create_standard()
        elif user_k == 2:
            return self.create_custom()
        else:
            raise ValueError('Oops!')
    
    def create_standard(self) -> DomainEvent:
        print('\nCreating standard Contract event.')
        for k in standard_event_dict:
            print(f'{k}: {standard_event_dict[k].description}')

        print('\n')
        kl = list(standard_event_dict.keys())
        for i,k in enumerate(kl):
            print(f'{i+1}: {k}')
        
        user_k = int(input('Selection #: '))
        sel_k = kl[user_k - 1]

        domain_event = standard_event_dict[sel_k].domain_event
        new_event = copy.deepcopy(domain_event)
        return new_event


    def create_custom(self) -> DomainEvent:
        verb = self._get_verb()
        frame = self._get_frame(verb)

        if frame is None:
            event_props = self._handle_custom_frame()
        else:
            frame_elements = self._get_frame_elements(frame)
            event_props = self._get_event_props(frame_elements)

        event_name = f'{verb.capitalize()}'
        return DomainEvent(event_name, event_props)

    
    def _get_verb(self) -> str:
        my_verb = input('enter verb:')
        # TODO: Validation?
        # Formatting... e.g. snake-case etc
        return my_verb

    def _get_frame(self, my_verb:str) -> AttrDict:
        regex_string = r'^' + my_verb
        frame_lus = self.__fn.lus(regex_string)

        verb_flus = [f for f in frame_lus if f.POS == 'V']

        if len(verb_flus) == 0:
            return None

        for i, flu in enumerate(verb_flus):
            print(f'{i+1}: {flu.name} - {flu.definition}')
        
        f_key = input('select the desired definition # (or leave blank for custom): ')

        if not f_key:
            return None

        target_flu = verb_flus[int(f_key)-1]

        return target_flu.frame

    def _handle_custom_frame(self):
        return self._get_custom_props()

    def _get_frame_elements(self, frame: AttrDict) -> Dict[str, AttrDict]:
        all_fes: PrettyDict = frame.FE
        core_keys = [k for k in all_fes if all_fes[k].coreType == 'Core']
        target_fes = {k: all_fes[k] for k in core_keys}
        return target_fes
    
    def _get_event_props(self, frame_elements) -> List[DomainProp]:
        results: List[DomainProp] = []
        
        props1 = self._get_props_from_frames(frame_elements)
        results.extend(props1)
        props2 = self._get_custom_props()
        results.extend(props2)
        
        return results

    def _get_props_from_frames(self, frame_elements) -> List[DomainProp]:
        results: List[DomainProp] = []
        
        for k in frame_elements:
            fe = frame_elements[k]
            print(f'Property: {fe.name}')
            print(f'- definition: {fe.definition}')

            keep_prop_key = input(f'Keep property (y/n): ')
            if keep_prop_key != 'y':
                continue

            prop_name = input(f'Enter new prop name (or leave blank if \'{fe.name}\' is okay: ') or fe.name
            prop_type = self._select_type()

            next_prop = DomainProp(prop_name, prop_type)
            results.append(next_prop)
        
        return results


    def _get_custom_props(self) -> List[DomainProp]:
        results: List[DomainProp] = []

        while (True):
            next_prop_name = input('Enter a new prop name (or leave blank if done): ')
            if not next_prop_name:
                break
            
            prop_type = self._select_type()
            new_prop = DomainProp(next_prop_name, prop_type)
            results.append(new_prop)

        return results
    
    def _select_type(self):
        print('Select the property type:')
        for i, pt in enumerate(self.__prop_types):
            print(f'{i+1}: {pt}')
        
        pt_key = input('Enter #:')
        prop_type = self.__prop_types[int(pt_key) - 1]

        return prop_type


