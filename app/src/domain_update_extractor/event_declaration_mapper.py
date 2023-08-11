from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.spec.declaration import IDeclaration, Declaration, EventDeclaration, DeclarationProp
from app.classes.events.custom_event.verb import VerbType

from app.src.domain_update_extractor.declaration_prop_mapper import IMapDeclarationProps


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
        
        
        if VerbType.INTRANSITIVE in verb.verb_types:
            result = self._map_intransitive(evt)

        # Transitive verb
        if VerbType.TRANSITIVE in verb.verb_types:
            result = self._map_transitive(evt)
        
        return result
    

    def _map_linking(self, evt: CustomEvent) -> IDeclaration:
        name = evt.get_declaration_name()
        props = []
        if evt.subj.is_role:
            agent_prop = DeclarationProp('agent', evt.subj.str_val, 'Role')
            props.append(agent_prop)

        pps = self._map_pps(evt)
        props.extend(pps)
        return EventDeclaration(evt.event_key(), name, props)
    

    def _map_intransitive(self, evt: CustomEvent) -> EventDeclaration:
        name = evt.get_declaration_name()

        p1 = self.__prop_mapper.map_subject(evt.subj, evt)
        
        return EventDeclaration(evt.event_key(), name, [p1])
    

    def _map_transitive(self, evt: CustomEvent) -> IDeclaration:
        name = evt.get_declaration_name()
        
        p1 = self.__prop_mapper.map_subject(evt.subj, evt)
        p2 = self.__prop_mapper.map_dobject(evt.dobj, evt)

        pps = self._map_pps(evt)
        
        props = [p1, p2]
        props.extend(pps)
        
        return EventDeclaration(evt.event_key(), name, props)


    def _map_pps(self, evt: CustomEvent):
        pps = []
        if evt.pps:
            pps = [self.__prop_mapper.map_prep_phrase(x, evt) for x in evt.pps]
        
        return pps
