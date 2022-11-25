from app.src.rules.shared.score_based_extractor import ScoreBasedExtractor
from app.src.rules.shared.basic_scorer import BasicScorer
from app.src.rules.meat_sale.payment_amount.currency_scorer import CurrencyScorer
from app.src.rules.meat_sale.payment_amount.amount_scorer import AmountScorer
from app.src.rules.meat_sale.interest_amount.percent_scorer import PercentScorer
from app.src.rules.meat_sale.payment_amount.matchers import get_validation_matcher
from app.src.rules.shared.match_validator import MatchValidator
from app.src.rules.shared.property_similarity_scorer import PropertySimilarityScorer
from app.src.rules.shared.domain_reference_scorer import DomainReferenceScorer

def get_ia_libs(nlp):
    matcher = get_validation_matcher(nlp)

    validator = MatchValidator(matcher)
    prop_scorer = PropertySimilarityScorer(nlp)

    # Currency
    allowed_currs = ['USD', 'CAD'] # Get this from the domain model
    currency_scorer = CurrencyScorer(allowed_currs)
    reference_scorer = DomainReferenceScorer(nlp, 'currency', prop_scorer)
    currency_scorers = [
        BasicScorer('X', 0),
        currency_scorer,
        reference_scorer
    ]
    currency_extractor = ScoreBasedExtractor(nlp, validator, currency_scorers)

    # Amount
    amount_scorer = AmountScorer(nlp)
    percent_scorer = PercentScorer(nlp, prop_scorer)
    amount_scorers = [
        BasicScorer('0', 0),
        amount_scorer,
        percent_scorer
    ]
    amount_extractor = ScoreBasedExtractor(nlp, validator, amount_scorers)

    return {
        'currency_extractor': currency_extractor,
        'amount_extractor': amount_extractor
    }

