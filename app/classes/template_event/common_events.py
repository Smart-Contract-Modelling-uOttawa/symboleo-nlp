from typing import Dict
from app.classes.spec.domain_object import DomainEvent, DomainProp, EventNLTemplate
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.verb import Verb, VerbType, VerbConjugations
from app.classes.custom_event.adverb import Adverb
from app.classes.template_event.EventMapping import EventMapping


from string import Template

# class CommonEvent: 
#     def __init__(self, domain_event:DomainEvent, description:str):
#         self.domain_event = domain_event
#         self.description = description

class CommonDomainEvents:
    provide_termination_notice = lambda: \
        DomainEvent('ProvideTerminationNotice', [
            DomainProp('agent', 'Role'),
            DomainProp('daysInAdvance', 'Number')
        ],
        # Ok so actually... this may need to be a CustomEvent... need conjugation
        ## Or we need another converter somewhere. Has to link to CustomEvent somehow
        EventNLTemplate('')
        )

class CommonCustomEvents:
    provide_termination_notice = lambda: \
        CustomEvent(
            subj = NounPhrase(), #.... This is what needs filling
            verb = Verb('provides', 'provide', [VerbType.TRANSITIVE], VerbConjugations('provide', 'provides', 'provided', 'providing')),
            dobj = NounPhrase('termination notice', 'notice', adjs=['termination']),
            adverb = Adverb('X days in advance')
        )


# Mapping will tell us what needs to be filled in
# Can also give a value to start us off. E.g. each one could be a Template/prompt
# User picks the event (based on a description)
# Then iterates through the domain properties (key/type) - user fills them out
# Then we need a mapping from DomainEvent to CustomEvent
mapping = {
    'subject': Template('$name'),
    'adverb':  Template('$num $unit in advance') # Also want to specify the types of these (numbers, options,...)
}

sample_mapping = {
    'role': Template('$name'),
    'daysInAdvance': Template('$num $unit in advance')
}

actual_mapping = {
    'role': EventMapping('subject', Template('$name')),
    'timeInAdvance': ('adverb', Template('$num $unit in advance'))
}

# Have a template 
class CommonTemplate:
    # Links to a customEvent
    # And has a list of what is missing
    # And a render function
    def __init__(self, evt: CustomEvent, mapping: Dict):
        self.evt = evt
        self.mapping = mapping
    

            # Add all the possibl inputs to each template rendering
            # Will likely need to use the safe substitute... since we'll be overkilling
            #  



# Need to map it to a CustomEvent... But I need a way for the nl template to say what is required
## I think thats the point of the CommonEvent - it has a function
## But we'll want to program this for the decl to domain mapper. 
## Well in that case I think it will just be everything
    
# Ok, so how does the user fill it in though
## They select the event they want (provide_termination_notice)
## Prompts them to input: name, then timespan
## For each of these, need a Template and types for the value

class InputReq:
    def __init__(self, str_template: Template, evt_component:str, val_type:str):
        self.str_template = str_template
        self.evt_component = evt_component
        self.val_type = val_type # May even be a nodetype...


# key is domain prop, value is template?
input_needs = {
    'agent': InputReq(Template('$name'), 'subject', 'NounPhrase'),
    'time_in_advance': InputReq(Template('$timespan in advance'), 'adverb', 'Adverb')
}

class FillItOut:
    def run():
        # Choose the common event
        # So we have a domain_event and a customevent
        domain_event = DomainEvent()
        custom_event = CustomEvent()

        # Fetch the required info
        result_set = {}

        for ik in input_needs:
            input_need = input_needs[ik]
            print(ik, input_need.str_template)

            # Gather user input
            user_input = input('Enter required value: ')

            # Run extractor to get the object (use the input_need.val_type for a dict)
            val = None

            result_set[input_need.evt_component] = val

        # Now we hav the result_set
        custom_event = CommonCustomEvents.provide_termination_notice() # Can have a dict for this

        for rk in result_set:
            the_obj = result_set[rk]
            if rk == 'subject':
                custom_event.subj = the_obj
            ###


# the thing is, im sorta recreating the entire process that I started with, but internally
## basically the node thing
## So can I just treat it as a set of nodes

# User picks common event. Then they choose an option
## This gives them a prefilled CustomEvent
## This has a set of subsequent nodes that it picks
## We're making an event, but we just have some pre-built pieces of it...
## Need to specify a set of nodes (as the children), and then get ahold of the custom_event
## Need that initial value for the update_obj or something
## Could be part of the get_children...
## Or it just has a controller that auto-fills some of the nodes

## Ok maybe were on to something
## Select the commonEvent
## Provides a list of SelectedNodes and their values that make up an event
## This helps to build the child node, 

# For each of the input needs
## Present the template of what is needed
## ** Can we iterate through the template?
## User will input the name
## Will extract the value -> NounPhrase. Can use the value_extractor dict again maybe?
## User will input the timespan. Fill the template




# # To build up this list, should do a verb search on the cuad set to find the most common verbs
# standard_event_dict: Dict[str, StandardEvent] = {
#     'breach_agreement': StandardEvent(
#         DomainEvent('BreachAgreement', [
#             DomainProp('breacher', 'Role')
#         ]),
#         'Event when one party (breacher) fails to complete any obligation.'
#     ),

#     # TODO: args should use a timespan: time_unit and time_value
#     'provide_termination_notice': StandardEvent(
#         DomainEvent('ProvideTerminationNotice', [
#             DomainProp('agent', 'Role'),
#             DomainProp('daysInAdvance', 'Number')
#         ]),
#         'One party (agent) provides notice a certain number of days in advance to terminate a contract'
#     )
    
# }
