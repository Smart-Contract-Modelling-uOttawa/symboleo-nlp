from app.classes.spec.declaration import Declaration
from app.classes.template_event.common_event import CommonEvent

# Move to SRC...
class IMapCommonEvents:
    def map(self, evt: CommonEvent) -> Declaration:
        raise NotImplementedError()

# May have a default..

