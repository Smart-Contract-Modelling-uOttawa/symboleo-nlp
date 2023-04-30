from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.verb import Verb, VerbType, VerbConjugations
from app.classes.custom_event.adverb import Adverb
from app.classes.custom_event.predicate import Predicate
from app.classes.custom_event.prep_phrase import PrepPhrase

from app.classes.template_event.common_event import CommonEvent

class CommonEvents:
    provide_termination_notice = lambda: \
        CommonEvent(
            subj = None,
            verb = Verb('provides', 'provide', [VerbType.TRANSITIVE], VerbConjugations('provide', 'provides', 'provided', 'providing')),
            dobj = NounPhrase('termination notice', 'notice', adjs=['termination']),
            adverb = Adverb('X days in advance'), # TODO: I'd like to capture this somehow
            common_event_key='provide_termination_notice'
        )

# Maybe I shouldnt init it...
COMMON_EVENT_DICT = {
    'provide_termination_notice': CommonEvents.provide_termination_notice()
}