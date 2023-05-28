from typing import List
from app.classes.units.input_unit import InputUnit
from app.classes.units.node_type import NodeType

from app.classes.elements.domain_timepoint_node import DomainTimepointNode as Target

class DomainTimepointNode(InputUnit):
    node_type = NodeType.DOMAIN_TIMEPOINT
    sn_type = Target
    prompt = 'Domain timepoint...'
    needs_value = True
    
    # TODO: Not sure how this will work, especially with options..
    ## Might init with the contract...
    # def __init__(self, id: str, children: List[InputUnit] = [], init_value: str = ''):
    #     super().__init__(id, children)
    #     self.prompt = init_value
    #     self.init_value = init_value

    
