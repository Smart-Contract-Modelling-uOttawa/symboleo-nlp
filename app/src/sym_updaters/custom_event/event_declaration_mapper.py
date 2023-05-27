
from typing import List
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.spec.declaration import IDeclaration, Declaration, DeclarationProp
from app.classes.custom_event.verb import VerbType

from app.src.helpers.string_to_class import CaseConverter
from app.src.sym_updaters.custom_event.declaration_prop_mapper import IMapDeclarationProps


class IMapEventToDeclaration:
    def map(self, evt: CustomEvent) -> IDeclaration:
        raise NotImplementedError()

class EventDeclarationMapper(IMapEventToDeclaration):
    def __init__(self, prop_mapper: IMapDeclarationProps):
        self.__prop_mapper = prop_mapper

    def map(self, evt: CustomEvent) -> IDeclaration:
        verb = evt.verb
        result = None

        # Linking verb
        if VerbType.LINKING in verb.verb_types and len(verb.verb_types) == 1:
            result = self._map_linking(evt)
        
        # Transitive verb
        if VerbType.TRANSITIVE in verb.verb_types:
            result = self._map_transitive(evt)

        # TODO: Intransitive
        


        return result
    

    def _map_linking(self, evt: CustomEvent) -> IDeclaration:
        subj = evt.subj
        pred = evt.predicate
        name = CaseConverter.to_pascal(f'{subj.to_text()} {pred.pred_str}')

        pps = self._map_pps(evt)

        snake_name = CaseConverter.to_snake(name)
        return Declaration(f'evt_{snake_name}', name, 'events', pps)
    

    def _map_transitive(self, evt: CustomEvent) -> IDeclaration:
        name = evt.verb.lemma.title()

        if evt.adverb:
            name = f'{name}{evt.adverb.adverb_str.title()}'
        
        p1 = self.__prop_mapper.map_subject(evt.subj, evt)
        p2 = self.__prop_mapper.map_dobject(evt.dobj, evt)

        pps = self._map_pps(evt)
        
        props = [p1, p2]
        props.extend(pps)


        snake_name = CaseConverter.to_snake(name)
        return Declaration(f'evt_{snake_name}', name, 'events', props)


    def _map_pps(self, evt: CustomEvent):
        pps = []
        if evt.pps:
            pps = [self.__prop_mapper.map_prep_phrase(x, evt) for x in evt.pps]
        
        return pps
