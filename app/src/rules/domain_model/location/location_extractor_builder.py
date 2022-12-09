from app.src.rules.domain_model.score_based_extractor import ScoreBasedExtractor
from app.src.rules.domain_model.location.address_scorer import AddressScorer
from app.src.rules.domain_model.location.noun_chunk_scorer import NounChunkScorer
from app.src.rules.domain_model.basic_scorer import BasicScorer
from app.src.rules.domain_model.location.role_scoring.role_scorer import RoleScorer
from app.src.rules.domain_model.property_similarity_scorer import PropertySimilarityScorer
from app.src.rules.domain_model.similarity_scorer import SimilarityScorer

from app.src.rules.domain_model.location.role_scoring.role_coref_dict_builder import RoleCorefDictBuilder
from app.src.rules.domain_model.location.role_scoring.role_match_dict_builder import RoleMatchDictBuilder

from app.src.rules.shared.match_validator import MatchValidator
from app.src.rules.domain_model.location.address_extractor import AddressExtractor
from app.src.rules.domain_model.location.role_scoring.role_score_builder import RoleScoreBuilder
from app.src.rules.domain_model.location.coref_getter import CorefGetter
from app.src.rules.domain_model.location.role_scoring.coref_template_prepper import CorefTemplatePrepper
from app.src.rules.domain_model.location.matchers import get_validation_matcher

from app.src.matcher_helper import MyMatcher
from app.src.rules.domain_model.location.role_scoring.role_pattern_builder import RolePatternBuilder
from app.src.rules.domain_model.location.location_span_extractor import LocationSpanExtractor
from app.src.rules.domain_model.location.role_scoring.role_score_assembler import RoleScoreAssembler

from app.src.rules.shared.interfaces import IBuildPropertyExtractor, IExtractProperties

class LocationExtractorBuilder(IBuildPropertyExtractor):
    @staticmethod
    def build(nlp) -> IExtractProperties:
        # This will need to be passed in
        init_role_scores = {
            'buyer': 0.6,
            'seller': 0.4
        }
        
        address_extractor = AddressExtractor()

        role_pattern_builder = RolePatternBuilder()
        matcher = MyMatcher(nlp)
        role_match_dict_builder = RoleMatchDictBuilder(init_role_scores, role_pattern_builder, matcher)
        
        coref_getter = CorefGetter(nlp)
        coref_prepper = CorefTemplatePrepper(nlp)
        role_coref_dict_builder = RoleCorefDictBuilder(init_role_scores, coref_prepper, coref_getter)
        inner_scorers = [
            role_match_dict_builder,
            role_coref_dict_builder
        ]
        role_score_builder = RoleScoreBuilder(init_role_scores, inner_scorers)
        
        location_span_extractor = LocationSpanExtractor()

        similarity_scorer = SimilarityScorer()
        prop_scorer = PropertySimilarityScorer(nlp, similarity_scorer)
        role_score_assembler = RoleScoreAssembler(prop_scorer)

        scorers = [
            BasicScorer('buyer', 0),
            NounChunkScorer(nlp),
            AddressScorer(nlp, address_extractor),
            RoleScorer(location_span_extractor, role_score_builder, role_score_assembler)
        ]

        v_matcher = get_validation_matcher(nlp)
        validator = MatchValidator(v_matcher)
        location_extractor = ScoreBasedExtractor(nlp, validator, scorers)

        return location_extractor


