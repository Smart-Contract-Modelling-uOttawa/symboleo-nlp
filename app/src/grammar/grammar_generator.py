from typing import List
from app.classes.symboleo_contract import SymboleoContract, ContractSpec, DomainEvent
from app.classes.grammar.grammar_nodes.all_nodes import *
from app.classes.spec.sym_event import ContractEventName, ObligationEventName, PowerEventName

from app.src.grammar.helpers.domain_timepoint_extractor import IExtractDomainTimePoints
from app.src.grammar.grammar_config import GrammarGeneratorConfig, ParmOpCode

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
        domain_model = contract.domain_model
        contract_spec = contract.contract_spec

        # Event names
        #domain_event_names = [x for x in domain_model.events] 
        domain_event_names = self._get_domain_event_names(contract_spec)

        obligation_names = [x for x in contract_spec.obligations] # TODO: Need surviving obligtions as well...
        power_names = [x for x in contract_spec.powers]

        # Timepoints
        ## TODO: Actually, should be getting this from the declarations; not the domain model...
        decl_event_timepoints = self.__domain_timepoint_extractor.extract(contract)

        ## CONTRACT EVENTS ##
        # Contract Event Actions
        contract_event_action_nodes = [
            ContractEventActionNode(f'ContractEvent.event_name.{x}', [], x) 
            for x in self.__contract_actions
        ]

        # ContractEvent
        contract_event_node = ContractEventNode('ContractEvent', contract_event_action_nodes)

        ## DOMAIN EVENTS ##
        ## Domain Event Action
        domain_event_name_nodes = [
            DomainEventNameNode(f'DomainEvent.event_name.{x}', [], x)
            for x in domain_event_names
        ]

        # Domain Event
        domain_event_node = DomainEventNode('DomainEvent', domain_event_name_nodes)

        ## OBLIGATION EVENTS ##
        # Obligation Event Action
        obligation_action_nodes = [
            ObligationEventActionNode(f'ObligationEvent.event_name.{x}', [], x)
            for x in self.__obligation_actions
        ]

        # Obligation Variable Name
        obligation_name_nodes = [
            ObligationEventVarNode(f'ObligationEvent.ob_var.{x}', obligation_action_nodes, x)
            for x in obligation_names
        ]

        # ObligationEvent
        obligation_event_node = ObligationEventNode('ObligationEvent', obligation_name_nodes)
        
        ## EVENT ##
        event_node = EventNode(
            'Event', 
            [obligation_event_node, contract_event_node, domain_event_node]
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

        ## USING ##
        instrument_node = InstrumentNode('Instrument')

        using_node = UsingNode('Using', [instrument_node])

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
        
        if ParmOpCode.ADD_DM_PROP in config.op_codes:
            root_children.append(using_node)

        root_node = RootNode('Root', root_children)
        
        return root_node

    def _get_domain_event_names(self, contract_spec: ContractSpec) -> List[str]:
        return [x.name for x in list(contract_spec.declarations.values()) if x.base_type == 'events']
