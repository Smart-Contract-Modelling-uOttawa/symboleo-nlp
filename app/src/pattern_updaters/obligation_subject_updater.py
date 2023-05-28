from app.classes.elements.standard_event_node import ObligationSubjectNode
from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.custom_event.noun_phrase import NounPhrase

from app.src.pattern_updaters.pattern_updater import IUpdatePattern 

class ObligationSubjectUpdater(IUpdatePattern):
    def update(self, node: ObligationSubjectNode, pattern: EventPattern):
        # May potentially make an ObligationNounPhrase that inherits from NounPhrase...

        # TODO: Ok, this is where it will get tricky... Need to extract the event from here...

        ob_var = node.value.str_val
        

        # Then we need to go to the contract and get it. So contract needs to be passed in... damn
        # Then suppose we have the obligation... (norm)
        # That will have a predicate in the consequent e.g. Happens(EVT_X)
        # This gives us a link to the declaration. So we can get a declaration
        # Then we need to turn the declaration into a NL event - this is a challenge...
        ## Then we would need to add the NOT in if its violated.  
        
        # Essentially this will set everything on the frame.event
        ## Need to map Declaration to CustomEvent...
        ## We have an event_declaration_mapper... now I guess we need the opposite as well

        subj = NounPhrase(
            str_val = node.value.to_text(),
            head = node.value.to_text()
        )
        pattern.event.subj = subj
