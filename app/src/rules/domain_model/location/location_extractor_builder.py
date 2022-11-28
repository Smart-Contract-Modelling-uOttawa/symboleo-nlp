from app.src.rules.domain_model.score_based_extractor import ScoreBasedExtractor
from app.src.rules.domain_model.location.address_scorer import AddressScorer
from app.src.rules.domain_model.location.noun_chunk_scorer import NounChunkScorer
from app.src.rules.domain_model.basic_scorer import BasicScorer
from app.src.rules.domain_model.location.role_scorer import RoleScorer
from app.src.rules.domain_model.property_similarity_scorer import PropertySimilarityScorer

from app.src.rules.shared.match_validator import MatchValidator
from app.src.rules.domain_model.location.address_extractor import AddressExtractor
from app.src.rules.domain_model.location.role_score_builder import RoleScoreBuilder
from app.src.rules.domain_model.location.coref_getter import CorefGetter
from app.src.rules.domain_model.location.matchers import get_validation_matcher

from app.src.rules.shared.interfaces import IBuildPropertyExtractor, IExtractProperties

class LocationExtractorBuilder(IBuildPropertyExtractor):
    @staticmethod
    def build(nlp) -> IExtractProperties:
        # This will need to be passed in
        init_role_scores = {
            'buyer': 0.6,
            'seller': 0.4
        }

        coref_getter = CorefGetter(nlp)
        address_extractor = AddressExtractor()
        role_score_builder = RoleScoreBuilder(nlp, init_role_scores, coref_getter)
        prop_scorer = PropertySimilarityScorer(nlp)

        scorers = [
            BasicScorer('buyer', 0),
            NounChunkScorer(nlp),
            AddressScorer(nlp, address_extractor),
            RoleScorer(nlp, role_score_builder, prop_scorer)
        ]

        v_matcher = get_validation_matcher(nlp)
        validator = MatchValidator(v_matcher)
        location_extractor = ScoreBasedExtractor(nlp, validator, scorers)

        return location_extractor


