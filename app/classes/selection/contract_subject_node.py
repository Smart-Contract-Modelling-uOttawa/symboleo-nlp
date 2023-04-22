from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

from app.classes.custom_event.noun_phrase import NounPhrase

class ContractSubjectNode(SelectedNode[NounPhrase]):
    node_type = NodeType.CONTRACT_SUBJECT

