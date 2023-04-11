from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract

class IExtractDomainTimePoints:
    def extract(self, contract: SymboleoContract) -> List[str]:
        raise NotImplementedError()

class DomainTimepointExtractor(IExtractDomainTimePoints):
    def extract(self, contract: SymboleoContract) -> List[str]:
        results = []
        all_events = [x for x in contract.contract_spec.declarations.values() if x.base_type == 'events']

        for event_decl in all_events:
            date_props = [x for x in event_decl.props if x.type == 'Date']

            for dp in date_props:
                next_val = f'{event_decl.name}.{dp.key}'
                results.append(next_val)

        return results

