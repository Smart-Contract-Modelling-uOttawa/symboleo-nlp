from app.classes.events.custom_event.verb import Verb, VerbConjugations, VerbType

class VerbStore:
    pay = lambda: Verb('pays', 'pay', [VerbType.TRANSITIVE], VerbConjugations('pay', 'pays', 'paid', 'paying'))
    