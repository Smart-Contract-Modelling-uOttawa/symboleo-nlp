from app.src.update_processor.declaration_prop_mapper import DeclarationPropMapper
from app.src.update_processor.event_declaration_mapper import EventDeclarationMapper

class EventDeclarationMapperBuilder:
    @staticmethod
    def build() -> EventDeclarationMapper:
        prop_mapper = DeclarationPropMapper()
        return EventDeclarationMapper(prop_mapper)