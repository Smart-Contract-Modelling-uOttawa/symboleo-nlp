from app.src.operations.refine_parameter2.parameter_refiner import ParameterRefiner 
from app.src.frames.frame_builder_builder import FrameBuilderBuilder
from app.src.updaters.updater_dict import UpdaterDictConstructor
from app.src.operations.refine_parameter2.update_extractor import UpdateExtractor

from app.src.operations.dependencies import Dependencies

class ParameterRefinerConstructor:
    @staticmethod
    def construct(deps: Dependencies) -> ParameterRefiner:
        frame_builder = FrameBuilderBuilder.build()
        updater_dict = UpdaterDictConstructor.build(deps)
        update_extractor = UpdateExtractor(updater_dict)

        return ParameterRefiner(frame_builder, update_extractor)
