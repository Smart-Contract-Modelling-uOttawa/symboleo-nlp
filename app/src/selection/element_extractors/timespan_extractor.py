from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.elements.timespan import Timespan
from app.classes.spec.point_function import TimeUnit
from app.src.selection.element_extractors.value_extractor import IExtractValue

class TimespanExtractor(IExtractValue[Timespan]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> Timespan:
        time_value, time_unit = str_val.split(' ')
        return Timespan(time_value, TimeUnit[time_unit.capitalize()])
