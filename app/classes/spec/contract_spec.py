from __future__ import annotations
from typing import Dict, List
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.declaration import Declaration
from app.classes.spec.norm import Obligation, Power
from app.classes.spec.proposition import Proposition
from app.classes.other.helpers import ClassHelpers

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
        self.parameters = parameters
        self.declarations = declarations
        self.preconditions = preconditions
        self.postconditions = postconditions
        self.obligations = obligations
        self.surviving_obligations = surviving_obligations
        self.powers = powers
        self.constraints = constraints

    def __eq__(self, other: ContractSpec) -> bool:
        return self.id == other.id and \
            ClassHelpers.lists_eq(self.parameters, other.parameters, 'name') and \
            ClassHelpers.dicts_eq(self.declarations, other.declarations) and \
            ClassHelpers.dicts_eq(self.obligations, other.obligations) and \
            ClassHelpers.dicts_eq(self.surviving_obligations, other.surviving_obligations) and \
            ClassHelpers.dicts_eq(self.powers, other.powers)
            #ClassHelpers.lists_eq(self.preconditions, other.preconditions, 'name') and \
            #ClassHelpers.lists_eq(self.postconditions, other.postconditions, 'name') and \
            #ClassHelpers.lists_eq(self.constraints, other.constraints, 'name') and \
            
            
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