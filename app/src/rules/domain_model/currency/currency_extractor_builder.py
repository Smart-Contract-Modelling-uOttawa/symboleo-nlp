from app.src.rules.domain_model.score_based_extractor import ScoreBasedExtractor
from app.src.rules.domain_model.basic_scorer import BasicScorer
from app.src.rules.domain_model.currency.simple_currency_scorer import SimpleCurrencyScorer
from app.src.rules.domain_model.amount.matchers import get_validation_matcher
from app.src.rules.shared.match_validator import MatchValidator
from app.src.rules.domain_model.property_similarity_scorer import PropertySimilarityScorer
from app.src.rules.domain_model.domain_reference_scorer import DomainReferenceScorer

from app.src.rules.shared.interfaces import IBuildPropertyExtractor, IExtractProperties

class CurrencyExtractorBuilder(IBuildPropertyExtractor):
    @staticmethod
    def build(nlp) -> IExtractProperties:
        matcher = get_validation_matcher(nlp)

        validator = MatchValidator(matcher)
        prop_scorer = PropertySimilarityScorer(nlp)

        # Currency
        allowed_currs = ['USD', 'CAD'] # Get this from the domain model
        currency_scorer = SimpleCurrencyScorer(allowed_currs)
        reference_scorer = DomainReferenceScorer(nlp, 'currency', prop_scorer)
        currency_scorers = [
            BasicScorer('X', 0),
            currency_scorer,
            reference_scorer
        ]
        
        currency_extractor = ScoreBasedExtractor(nlp, validator, currency_scorers)
        
        return currency_extractor


