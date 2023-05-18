from app.src.sym_updaters.custom_event.declaration_prop_mapper import DeclarationPropMapper
from app.src.sym_updaters.custom_event.event_declaration_mapper import EventDeclarationMapper

class EventDeclarationMapperBuilder:
    @staticmethod
    def build() -> EventDeclarationMapper:
        prop_mapper = DeclarationPropMapper()
        return EventDeclarationMapper(prop_mapper)