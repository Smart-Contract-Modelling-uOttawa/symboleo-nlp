
from typing import List
from app.classes.other.frame_event import FrameEvent
from app.classes.spec.declaration import IDeclaration, Declaration, DeclarationProp
from app.classes.other.verb import VerbType

from app.src.helpers.string_to_class import CaseConverter

from app.src.nlp.frame_event.declaration_prop_mapper import IMapDeclarationProps


class IMapEventToDeclaration:
    def map(self, frame_event: FrameEvent) -> IDeclaration:
        raise NotImplementedError()

class EventDeclarationMapper(IMapEventToDeclaration):
    def __init__(self, prop_mapper: IMapDeclarationProps):
        self.__prop_mapper = prop_mapper


    def map(self, frame_event: FrameEvent) -> IDeclaration:
        verb = frame_event.verb

        # Linking verb
        if VerbType.LINKING in verb.verb_types and len(verb.verb_types) == 1:
            result = self._map_linking(frame_event)
        
        # Transitive verb
        if VerbType.TRANSITIVE in verb.verb_types:
            result = self._map_transitive(frame_event)

        # TODO: Intransitive

        return result
    

    # TODO: This needs to take assets and pps into account
    def _map_linking(self, frame_event: FrameEvent) -> IDeclaration:
        subj = frame_event.subj
        pred = frame_event.predicate
        name = CaseConverter.to_pascal(f'{subj.to_text()} {pred.pred_str}')

        pps = self._map_pps(frame_event)

        snake_name = CaseConverter.to_snake(name)
        return Declaration(f'evt_{snake_name}', name, 'events', pps)
    

    def _map_transitive(self, frame_event: FrameEvent) -> IDeclaration:
        name = frame_event.verb.lemma.title()

        if frame_event.adverb:
            name = f'{name}{frame_event.adverb.adverb_str.title()}'
        
        p1 = self.__prop_mapper.map_subject(frame_event.subj, frame_event)
        p2 = self.__prop_mapper.map_dobject(frame_event.dobj, frame_event)

        pps = self._map_pps(frame_event)
        
        props = [p1, p2]
        props.extend(pps)


        snake_name = CaseConverter.to_snake(name)
        return Declaration(f'evt_{snake_name}', name, 'events', props)


    def _map_pps(self, frame_event: FrameEvent):
        pps = []
        if frame_event.pps:
            pps = [self.__prop_mapper.map_prep_phrase(x, frame_event) for x in frame_event.pps]
        
        return pps