from app.classes.operations.dependencies import Dependencies

from app.src.custom_event_extractor.verb.verb_extractor import VerbExtractor
from app.src.custom_event_extractor.verb.fake_lemmatizer import FakeLemmatizer
from app.src.custom_event_extractor.verb.lemmatizer import Lemmatizer
from app.src.custom_event_extractor.verb.conjugator import MyConjugator
from app.src.custom_event_extractor.verb.conjugator import ML3Conjugator
from app.src.custom_event_extractor.noun_phrase.asset_type_extractor import AssetTypeExtractor
from app.src.custom_event_extractor.noun_phrase.noun_phrase_extractor import NounPhraseExtractor
from app.src.custom_event_extractor.noun_phrase.fake_noun_phrase_extractor import FakeNounPhraseExtractor
from app.src.custom_event_extractor.adverb_extractor import AdverbExtractor
from app.src.custom_event_extractor.predicate_extractor import PredicateExtractor
from app.src.custom_event_extractor.prep_phrase_extractor import PrepPhraseExtractor
from app.src.custom_event_extractor.custom_event_extractor import CustomEventExtractor

class CustomEventExtractorBuilder:
    @staticmethod
    def build(deps: Dependencies):
        if deps.fake:
            lemmatizer = FakeLemmatizer()
            np_extractor = FakeNounPhraseExtractor()
        else:
            lemmatizer = Lemmatizer(deps.nlp)
            asset_type_extractor = AssetTypeExtractor(deps.nlp)
            np_extractor = NounPhraseExtractor(deps.nlp, asset_type_extractor)

        inner_conjugator = ML3Conjugator(language = 'en')
        conjugator = MyConjugator(inner_conjugator)

        verb_extractor = VerbExtractor(lemmatizer, conjugator)

        pred_extractor = PredicateExtractor()

        advb_extractor = AdverbExtractor()

        pp_extractor = PrepPhraseExtractor(deps.nlp, np_extractor)


        return CustomEventExtractor(
            verb_extractor,
            np_extractor,
            advb_extractor,
            pred_extractor,
            pp_extractor,
        )
       
            
