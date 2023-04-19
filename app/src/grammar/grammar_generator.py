from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.norm import Obligation, Power
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration
from app.classes.tokens.all_nodes import *
from app.classes.spec.sym_event import ContractEventName, ObligationEventName, PowerEventName

from app.src.grammar.domain_timepoint_extractor import IExtractDomainTimePoints
from app.src.grammar.grammar_config import GrammarGeneratorConfig, ParmOpCode


# Will probably remove this. 
## Children will be generated upon selection... Since it can be infinite...
class IGenerateGrammar:
    def generate(self, contract: SymboleoContract) -> RootNode:
        raise NotImplementedError()

class GrammarGenerator(IGenerateGrammar):
    def __init__(
        self,
        domain_timepoint_extractor: IExtractDomainTimePoints
    ):
        self.__domain_timepoint_extractor = domain_timepoint_extractor

        # Symboleo State - should be loaded in
        self.__contract_actions = [x.value for x in ContractEventName]
        self.__obligation_actions = [x.value for x in ObligationEventName]
        self.__power_actions = [x.value for x in PowerEventName]

    # Pattern: Generator func, create the nodes, add to the node_dict
    def generate(self, contract: SymboleoContract, config: GrammarGeneratorConfig) -> RootNode:

        # Timepoints
        ## TODO: Actually, should be getting this from the declarations; not the domain model...
        decl_event_timepoints = self.__domain_timepoint_extractor.extract(contract)

        ## NEW EVENT ###
        new_event_node = NewEventNode('new_event', [])

        ## STANDARD EVENT ##
        standard_event_node = StandardEventNode('StandardEvent', [])

        ## EVENT ##
        ### Would like to join the contract/ob/power events - and maybe even the standard ones as well
        ### Then the "domain" event just becomes a custom one - results in a new domain object...
        event_node = EventNode(
            'Event', 
            [standard_event_node, new_event_node]
        )

        # timepoint_node 
        domain_timepoint_nodes = [DomainTimepointNode('TimepointNode.{x}', [], x) for x in decl_event_timepoints]
        timepoint_node = TimepointNode('Timepoint', domain_timepoint_nodes)

        ## DATE ##
        date_node = DateNode('Date')

        ## BEFORE ##
        before_node = BeforeNode('Before', [date_node, event_node, timepoint_node])

        ## AFTER ##
        after_node = AfterNode('After', [date_node, event_node])

        ## TIMESPAN ##
        timespan_node = TimespanNode('Timespan', [event_node])

        ## WITHIN ##
        ## Within 2 weeks of [Event]
        within_node = WithinNode('Within', [timespan_node])

        ## IF ##
        if_node = IfNode('If', [event_node])

        ## UNTIL ##
        until_node = UntilNode('Until', [event_node])

        ## ROOT ##
        root_children = []
        if ParmOpCode.ADD_TRIGGER in config.op_codes:
            root_children.append(if_node)
        
        if ParmOpCode.REFINE_PREDICATE in config.op_codes:
            root_children.append(before_node)
            root_children.append(after_node)
            root_children.append(within_node)
        
        if ParmOpCode.ADD_NORM in config.op_codes:
            root_children.append(until_node)

        root_node = RootNode('Root', root_children)
        
        return root_node


    def _get_domain_events(self, contract_spec: ContractSpec) -> List[Declaration]:
        result =  [x for x in list(contract_spec.declarations.values()) if x.base_type == 'events'] 
        return result
