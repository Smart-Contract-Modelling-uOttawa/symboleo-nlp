from app.classes.operations.dependencies import Dependencies

from app.src.selection.element_extractors.custom_event.verb.verb_extractor import VerbExtractor
from app.src.selection.element_extractors.custom_event.verb.fake_lemmatizer import FakeLemmatizer
from app.src.selection.element_extractors.custom_event.verb.lemmatizer import Lemmatizer
from app.src.selection.element_extractors.custom_event.verb.conjugator import MyConjugator
from app.src.selection.element_extractors.custom_event.verb.conjugator import ML3Conjugator
from app.src.selection.element_extractors.custom_event.noun_phrase.asset_type_extractor import AssetTypeExtractor
from app.src.selection.element_extractors.custom_event.noun_phrase.noun_phrase_extractor import NounPhraseExtractor
from app.src.selection.element_extractors.custom_event.noun_phrase.fake_noun_phrase_extractor import FakeNounPhraseExtractor
from app.src.selection.element_extractors.custom_event.adverb_extractor import AdverbExtractor
from app.src.selection.element_extractors.custom_event.predicate_extractor import PredicateExtractor
from app.src.selection.element_extractors.custom_event.prep_phrase_extractor import PrepPhraseExtractor


from app.src.update_processor2.domain_updates.custom_event_extractor import CustomEventExtractor

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
       
            
