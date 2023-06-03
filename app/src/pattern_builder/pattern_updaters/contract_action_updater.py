from app.classes.elements.standard_event_elements import ContractActionElement
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.events.custom_event.verb import Verb, VerbType, VerbConjugations
from app.classes.events.contract_events.standard_contract_event import StandardContractEvent

from app.classes.events.template_event.contract_components import ContractNouns, ContractVerbs

from app.src.pattern_builder.pattern_updaters.pattern_updater import IUpdatePattern 

class ContractActionUpdater(IUpdatePattern):
    def update(self, element: ContractActionElement, pattern: EventPattern):
        pattern.event = StandardContractEvent(element.value.value)
        val = element.input_value
        pattern.nl_event.verb = Verb(element.input_value, 'X', [VerbType.INTRANSITIVE], VerbConjugations(val,val,val,val))
            