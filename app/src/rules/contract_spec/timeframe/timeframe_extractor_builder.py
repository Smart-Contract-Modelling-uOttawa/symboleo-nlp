from typing import List

from app.src.rules.contract_spec.timeframe.timeframe_patterns import get_tf_patterns
from app.src.rules.contract_spec.all_primitive_scorer_builder import AllPrimitiveScorerBuilder
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.spec.p_atoms import PAtom
from app.classes.processing.components import AllParameters

from app.src.matcher_helper import MyMatcher
from app.src.graph.graph_builder import GraphBuilder
from app.src.rules.contract_spec.dynamic_constructor import DynamicObjectConstructor
from app.src.rules.shared.interfaces import IBuildPredicateExtractor, IExtractPredicates
from app.src.rules.contract_spec.predicate_extractor import PredicateExtractor
from app.src.rules.contract_spec.dynamic_constructor_builder import DynamicConstructorBuilder
from app.src.rules.contract_spec.all_primitives_scorer import AllPrimitivesScorer
from app.src.rules.contract_spec.parameter_scorer import ParameterScorer
from app.src.rules.contract_spec.predicate_scorer import PredicateScorer
from app.src.rules.contract_spec.pred_parm_combiner import PredParmCombiner
from app.src.rules.contract_spec.recursive_identifier import RecursiveParameterIdentifier

class TimeFrameExtractorBuilder(IBuildPredicateExtractor):
    @staticmethod
    def build(
        nlp, 
        template: PredicateFunction
    ) -> IExtractPredicates:

        templated_components = []
        for template_arg in template.__dict__:
            next_arg = template.__dict__[template_arg]
            templated_components.append(next_arg)

        case_patterns = get_tf_patterns(nlp)
        matcher = MyMatcher(nlp)
        predicate_scorer = PredicateScorer(case_patterns, matcher)

        primitive_scorer = AllPrimitiveScorerBuilder.build(nlp)
        
        graph_builder = GraphBuilder()
        digraph = graph_builder.build(PAtom)
        dynamic_constructor = DynamicObjectConstructor(digraph)
        recursive_identifier = RecursiveParameterIdentifier(digraph, dynamic_constructor)
        
        parameter_scorer = ParameterScorer(primitive_scorer, AllParameters, recursive_identifier, templated_components)
        
        combiner = PredParmCombiner(dynamic_constructor)

        return PredicateExtractor(predicate_scorer, parameter_scorer, combiner)

