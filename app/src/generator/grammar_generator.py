from app.classes.symboleo_contract import SymboleoContract
from app.classes.grammar.grammar_nodes.all_nodes import *

class IGenerateGrammar:
    def generate(self, contract: SymboleoContract) -> RootNode:
        raise NotImplementedError()

class GrammarGenerator(IGenerateGrammar):
    def __init__(self):
        # Symboleo State - should be loaded in
        self.__contract_actions = ['terminated', 'activated', 'suspended']
        self.__obligation_actions = ['suspended', 'triggered', 'completed', 'terminated successfully']
        self.__power_actions = []


    # Pattern: Generator func, create the nodes, add to the node_dict
    def generate(self, contract: SymboleoContract) -> RootNode:
        domain_model = contract.domain_model
        contract_spec = contract.contract_spec

        domain_event_names = [x for x in domain_model.events]
        obligation_names = [x for x in contract_spec.obligations]
        # power names = ...

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
            DomainEventNameNode('DomainEvent.event_name.{x}', [], x)
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
        
        ## DATE ##
        date_node = DateNode('Date')

        ## BEFORE ##
        before_node = BeforeNode('Before', [date_node, event_node])

        ## TIMESPAN ##
        timespan_node = TimespanNode('Timespan', [event_node])

        ## WITHIN ##
        ## Within 2 weeks of [Event]
        within_node = WithinNode('Within', [timespan_node])

        ## ROOT ##
        root_node = RootNode('Root', [before_node, within_node])
        
        return root_node
