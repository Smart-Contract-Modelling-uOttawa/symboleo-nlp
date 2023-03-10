from typing import List
from app.classes.symboleo_contract import SymboleoContract

class IExtractDomainTimePoints:
    def extract(self, contract: SymboleoContract) -> List[str]:
        raise NotImplementedError()

class DomainTimepointExtractor(IExtractDomainTimePoints):
    def extract(self, contract: SymboleoContract) -> List[str]:
        results = []
        all_events = contract.domain_model.events
        print('LLL', len(all_events))

        for dk in all_events:
            domain_obj = all_events[dk]
            date_props = [x for x in domain_obj.props if x.type == 'Date']
            print(dk, len(date_props))

            for dp in date_props:
                next_val = f'{domain_obj.name}.{dp.key}'
                print('---', next_val)
                results.append(next_val)

        return results

