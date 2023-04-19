from app.src.operations.refine_parameter2.parameter_refiner import ParameterRefiner 
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor 

from app.src.operations.refine_parameter2.parameter_refiner import ParameterRefiner
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor

from app.src.updaters.updater_dict import UpdaterDictConstructor
from app.src.operations.refine_parameter2.update_extractor import UpdateExtractor



class ParameterRefinerConstructor:
    @staticmethod
    def construct() -> ParameterRefiner:
        frame_checker = FrameCheckerConstructor.construct()
        updater_dict = UpdaterDictConstructor.build()
        update_extractor = UpdateExtractor(updater_dict)

        return ParameterRefiner(frame_checker, update_extractor)
