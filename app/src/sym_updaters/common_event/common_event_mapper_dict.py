from typing import Dict
from app.src.sym_updaters.common_event.i_map_common_events import IMapCommonEvents
from app.src.sym_updaters.common_event.provide_termination_mapper import ProvideTerminationMapper

class CommonEventMapperDictConstructor:
    # Passing in dependencies?
    @staticmethod
    def build() -> Dict[str, IMapCommonEvents]:
        
        # May have a default...
        return {
            'provide_termination_notice': ProvideTerminationMapper(),
            ###
        }