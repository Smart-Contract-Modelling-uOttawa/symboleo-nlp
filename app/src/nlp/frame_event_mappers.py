
from typing import List
from app.classes.other.frame_event import FrameEvent
from app.classes.spec.domain_object import IDomainObject, DomainEvent, DomainProp
from app.classes.spec.declaration import IDeclaration, Declaration, DeclarationProp

class IMapEventToDomain:
    def map(self, frame_event: FrameEvent) -> IDomainObject:
        raise NotImplementedError()


class DomainEventMapper(IMapEventToDomain):
    def map(self, frame_event: FrameEvent) -> IDomainObject:
        verb: str = frame_event.verb # Will be more complex
        
        domain_event_name = f'{verb.title()}' # PascalCase: VerbAdverb ?

        adverb: str = frame_event.adverb
        if adverb:
            domain_event_name += f'{adverb.title()}'

        # This is the interesting part...
        props: List[DomainProp] = [
            DomainProp('subj', 'String'),
            DomainProp('dobj', 'String')
        ]
        
        for i, x in enumerate(frame_event.pps):
            props.append(DomainProp(f'prep_{i+1}', 'String'))
        
        # Actually probably no event_text on the domain model
        return DomainEvent(domain_event_name, props, '')


class IMapEventToDeclaration:
    def map(self, frame_event: FrameEvent, domain_event: DomainEvent) -> IDeclaration:
        raise NotImplementedError()

class DeclarationEventMapper(IMapEventToDeclaration):
    def map(self, frame_event: FrameEvent, domain_event: DomainEvent) -> IDeclaration:
        fe = frame_event

        # This is the interesting part...
        props: List[DeclarationProp] = [
            DeclarationProp('subj', fe.subj, 'String'),
            #DeclarationProp('dobj', fe.dobj, 'String') # Only if transitive...
        ]

        if fe.dobj is not None:
            props.append(DeclarationProp('dobj', fe.dobj, 'String'))
        
        for i, x in enumerate(frame_event.pps):
            props.append(DeclarationProp(f'prep_{i+1}', x, 'String'))
        
        event_text = frame_event.to_text()

        #Snake case...
        declaration_name = f'evt_{domain_event.name}'
        
        return Declaration(declaration_name, 'events', domain_event.name, props, event_text)
