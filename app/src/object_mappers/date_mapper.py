from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.spec.norm_config import NormConfig
from app.classes.helpers.parm_checker import ParmChecker

class IMapDate:
    def map(self, date_text:str, pattern_class: PatternClass, norm_config: NormConfig) -> str:
        raise NotImplementedError()

class DateMapper(IMapDate):
    def map(self, date_text: str, pattern_variable: PV, norm_config: NormConfig) -> str:
        if ParmChecker.is_parm(date_text):
            return ParmChecker.lower_parm(date_text)
        
        if pattern_variable == PV.DATE:
            return f'{norm_config.norm.id}_date'

        if pattern_variable == PV.DATE2:
            return f'{norm_config.norm.id}_date2'
        
        raise ValueError('Pattern class is missing date') 


        