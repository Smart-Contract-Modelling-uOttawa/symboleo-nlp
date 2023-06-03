from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.elements.timespan import Timespan
from app.classes.spec.point_function import TimeUnit
from app.src.selection.element_extractors.element_extractor import IExtractElement

class TimespanExtractor(IExtractElement[Timespan]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> Timespan:
        time_value, time_unit = str_val.split(' ')
        return Timespan(int(time_value), TimeUnit[time_unit.capitalize()])
