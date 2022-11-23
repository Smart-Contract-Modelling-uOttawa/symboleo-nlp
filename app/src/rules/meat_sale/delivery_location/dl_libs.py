from app.src.rules.shared.score_based_extractor import ScoreBasedExtractor
from app.src.rules.meat_sale.delivery_location.address_scorer import AddressScorer
from app.src.rules.meat_sale.delivery_location.noun_chunk_scorer import NounChunkScorer
from app.src.rules.shared.basic_scorer import BasicScorer
from app.src.rules.meat_sale.delivery_location.role_scorer import RoleScorer

from app.src.rules.shared.match_validator import MatchValidator
from app.src.rules.meat_sale.delivery_location.address_extractor import AddressExtractor
from app.src.rules.meat_sale.delivery_location.role_score_builder import RoleScoreBuilder
from app.src.rules.meat_sale.delivery_location.coref_getter import CorefGetter
from app.src.rules.meat_sale.delivery_location.matchers import get_validation_matcher

def get_dl_libs(nlp):
    init_role_scores = {
        'buyer': 0.6,
        'seller': 0.4
    }

    coref_getter = CorefGetter(nlp)
    address_extractor = AddressExtractor()
    role_score_builder = RoleScoreBuilder(nlp, init_role_scores, coref_getter)

    scorers = [
        BasicScorer('buyer', 0),
        NounChunkScorer(nlp),
        AddressScorer(nlp, address_extractor),
        RoleScorer(nlp, role_score_builder)
    ]

    v_matcher = get_validation_matcher(nlp)
    validator = MatchValidator(v_matcher)
    location_extractor = ScoreBasedExtractor(nlp, validator, scorers)

    return {
        'location_extractor': location_extractor
    }


