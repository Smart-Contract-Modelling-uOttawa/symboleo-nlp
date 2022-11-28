from app.src.rules.domain_model.score_based_extractor import ScoreBasedExtractor
from app.src.rules.domain_model.basic_scorer import BasicScorer
from app.src.rules.domain_model.amount.amount_scorer import AmountScorer
from app.src.rules.domain_model.amount.percent_scorer import PercentScorer
from app.src.rules.domain_model.amount.matchers import get_validation_matcher
from app.src.rules.shared.match_validator import MatchValidator
from app.src.rules.domain_model.property_similarity_scorer import PropertySimilarityScorer

from app.src.rules.shared.interfaces import IBuildPropertyExtractor, IExtractProperties

class AmountExtractorBuilder(IBuildPropertyExtractor):
    @staticmethod
    def build(nlp) -> IExtractProperties:
        matcher = get_validation_matcher(nlp)

        validator = MatchValidator(matcher)
        prop_scorer = PropertySimilarityScorer(nlp)

        # Amount
        amount_scorer = AmountScorer(nlp)
        percent_scorer = PercentScorer(nlp, prop_scorer)
        amount_scorers = [
            BasicScorer('0', 0),
            amount_scorer,
            percent_scorer
        ]
        amount_extractor = ScoreBasedExtractor(nlp, validator, amount_scorers)

        return amount_extractor


