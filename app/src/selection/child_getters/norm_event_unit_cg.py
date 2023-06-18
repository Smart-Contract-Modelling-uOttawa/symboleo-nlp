from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

from app.classes.units.all_units import NormEventUnit, ObligationSubjectUnit

from app.src.selection.child_getters.child_getter import IGetUnitChildren

class NormEventUnitCG(IGetUnitChildren):
    def get(self, parent_unit: NormEventUnit, contract: SymboleoContract) -> List[InputUnit]:
        opts = []

        td = contract.nl_template.template_dict

        for nl_key in td:
            parms = td[nl_key].parameters
            for parm_key in parms:
                parm_list = parms[parm_key]
                for p in [x for x in parm_list if x.norm_type == 'obligations']:
                    opts.append(f'{nl_key}.{p.norm_id}')

        opts = list(dict.fromkeys(opts))

        # for x in contract.contract_spec.obligations:
        #     next_ob = contract.contract_spec.obligations[x]
        #     opts.append(next_ob.id)
        
        unit1 = ObligationSubjectUnit(opts)

        return [unit1]

