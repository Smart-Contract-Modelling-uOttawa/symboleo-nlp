# Should have a type for this...
# event_component

class EventMapping:
    def __init__(self, evt_component: str, the_object: any):
        self.evt_component = evt_component
        self.the_object = the_object