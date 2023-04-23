from app.classes.operations.dependencies import Dependencies

from app.src.operations.refine_parameter.parameter_refiner import ParameterRefiner
from app.src.frame_updaters.frame_builder_builder import FrameBuilderBuilder
from app.src.sym_updaters.sym_updater_dict import SymUpdaterDictConstructor
from app.src.sym_updaters.update_extractor import UpdateExtractor

class ParameterRefinerConstructor:
    @staticmethod
    def construct(deps: Dependencies) -> ParameterRefiner:
        frame_builder = FrameBuilderBuilder.build()
        updater_dict = SymUpdaterDictConstructor.build(deps)
        update_extractor = UpdateExtractor(updater_dict)

        return ParameterRefiner(frame_builder, update_extractor)
