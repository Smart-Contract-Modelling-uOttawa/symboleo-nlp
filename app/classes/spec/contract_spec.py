from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.declaration import Declaration
from app.classes.spec.norm import Obligation, Power
from app.classes.spec.proposition import Proposition
from app.classes.spec._sd import _sd


from typing import Dict, List


class ContractSpec:
    def __init__(
        self,
        id: str,
        parameters: List[ContractSpecParameter],
        declarations: Dict[str, Declaration],
        preconditions: List[Proposition],
        postconditions: List[Proposition],
        obligations: Dict[str, Obligation],
        surviving_obligations: Dict[str, Obligation],
        powers: Dict[str,Power],
        constraints: List[Proposition]
    ):
        self.id = id
        self.parameters = sorted(parameters, key=lambda x: x.name)
        self.declarations = _sd(declarations)
        self.preconditions = preconditions
        self.postconditions = postconditions
        self.obligations = _sd(obligations)
        self.surviving_obligations = _sd(surviving_obligations)
        self.powers = _sd(powers)
        self.constraints = constraints

    def to_sym(self):
        result = f'Contract {self.id}'
        parms_sym = ', '.join([x.to_sym() for x in self.parameters])
        result += f'( {parms_sym} )\n'


        result += '\nDeclarations\n'
        for x in self.declarations:
            result += f'  {self.declarations[x].to_sym()}\n'

        result += '\nPreconditions\n'
        for x in self.preconditions:
            result += f'  {x.to_sym()};\n'

        result += '\nPostconditions\n'
        for x in self.postconditions:
            result += f'  {x.to_sym()};\n'

        result += '\nObligations\n'
        for x in self.obligations:
            result += f'  {self.obligations[x].to_sym()}\n'

        result += '\nSurviving Obligations\n'
        for x in self.surviving_obligations:
            result += f'  {self.surviving_obligations[x].to_sym()}\n'

        result += '\nPowers\n'
        for x in self.powers:
            result += f'  {self.powers[x].to_sym()}\n'

        result += '\nConstraints\n'
        for x in self.constraints:
            result += f'  {x.to_sym()};\n'

        result += '\nendContract'
        return result