import copy
from typing import Dict, List
from app.classes.symboleo_contract import DomainModel
from app.classes.spec.domain_model import DomainProp, DomainEvent

import nltk
from nltk.corpus import framenet as fn
from nltk.corpus.reader.framenet import FramenetCorpusReader, AttrDict, PrettyDict

from app.src.nlp.standard_events import standard_event_dict
from app.src.nlp.framenet_extractor import FramenetExtractor

class DomainEventCreator:
    def __init__(self, domain_model: DomainModel):
        self.__fn_extractor = FramenetExtractor(fn)
        self.__prop_types = list(domain_model.assets.keys()) + list(domain_model.roles.keys()) + ['String', 'Number', 'Date', 'Role', 'Asset']

    def create(self) -> DomainEvent:
        print('Creating a new event.')
        print('1 - Choose from standard contract events')
        print('2 - Create a custom event')

        user_k = int(input('Select #: '))

        if user_k == 1:
            return self.create_from_standard()
        elif user_k == 2:
            return self.create_from_frame()
        else:
            raise ValueError('Oops!')
        
    
    def create_from_standard(self) -> DomainEvent:
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


    def create_from_frame(self) -> DomainEvent:
        my_verb = input('enter verb:') 
        # TODO: Validation? Will add a class to support this
    
        frame = self._get_frame(my_verb)

        if frame is None:
            event_props = self._handle_custom_frame()
        else:
            event_props = self._handle_found_frame()

        event_name = f'{my_verb.capitalize()}'
        return DomainEvent(event_name, event_props)


    def _get_frame(self, verb: str) -> AttrDict:
        flus = self.__fn_extractor.extract_flus_from_verb(verb)

        if len(flus) == 0:
            return None

        # Select the desired frame based on the definition
        for i, flu in enumerate(flus):
            print(f'{i+1}: {flu.name} - {flu.definition}')
        f_key = input('select the desired definition # (or leave blank for custom): ')

        # If user enters blank, then build a custom frame
        if not f_key:
            return None
    
        # Extract the frame
        frame = flus[int(f_key)-1].frame

        return frame


    def _handle_found_frame(self, frame: AttrDict):
        frame_elements = self.__fn_extractor.extract_core_fes(frame)

        results: List[DomainProp] = []

        frame_props = self._get_props_from_frames(frame_elements)
        results.extend(frame_props)
        
        custom_props = self._get_custom_props()
        results.extend(custom_props)
        
        return results


    def _handle_custom_frame(self):
        return self._get_custom_props()


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
    

    def _get_custom_props(self):
        results: List[DomainProp] = []

        while (True):
            next_prop_name = input('Enter a new prop name (or leave blank if done): ')
            if not next_prop_name:
                break
            
            prop_type = self._select_type()
            new_prop = DomainProp(next_prop_name, prop_type)
            results.append(new_prop)

        return results
    

    def _select_types(self):
        print('Select the property type:')
        for i, pt in enumerate(self.__prop_types):
            print(f'{i+1}: {pt}')
        
        pt_key = input('Enter #:')
        prop_type = self.__prop_types[int(pt_key) - 1]

        return prop_type
    