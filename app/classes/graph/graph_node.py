import copy

PROP_TYPE = 'prop'
SUBCLASS_TYPE = 'subclass'

class GraphNode:
    name: str = ''
    unit_type: str = '' # subclass or prop
    subclasses: list[str] = [] 
    props: list[str] = [] 

    def __init__(self, name, unit_type, subclasses, props):
        self.name = name
        self.unit_type = unit_type
        self.subclasses = copy.deepcopy(subclasses)
        self.props = copy.deepcopy(props)

    def __eq__(self, other): 
        if not isinstance(other, GraphNode):
            return NotImplemented

        return self.name == other.name and \
                self.unit_type == other.unit_type and \
                self._eq_list(self.subclasses, other.subclasses) and \
                self._eq_list(self.props, other.props)
    
    def _eq_list(self, a, b):
        if len(a) != len(b):
            return False
        
        return set(a) == set(b)
        

    def print_me(self, d=0):
        print(f'{self.name}')
        s_list = ','.join(self.subclasses)
        p_list = ','.join(self.props)
        print(f'-- s: {s_list}')
        print(f'-- p: {p_list}')
        

# Need to keep this updated
test_graph = {
    'PAtomPredicate': GraphNode(
        'PAtomPredicate',
        'ROOT',
        [],
        ['PredicateFunction']
    ),
    'PredicateFunction': GraphNode(
        'PredicateFunction',
        PROP_TYPE,
        [
            'PredicateFunctionHappens', 
            'PredicateFunctionHappensWithin', 
            'PredicateFunctionWHappensBefore', 
            'PredicateFunctionSHappensBefore', 
            'PredicateFunctionWHappensBeforeEvent',
            'PredicateFunctionSHappensBeforeEvent',
            'PredicateFunctionHappensAfter',
            'PredicateFunctionOccurs'
        ],
        []
    ),
    
    ## Predicate Functions ##
    'PredicateFunctionHappens': GraphNode(
        'PredicateFunctionHappens',
        SUBCLASS_TYPE,
        [],
        ['SymEvent']
    ),
    'PredicateFunctionWHappensBefore': GraphNode(
        'PredicateFunctionWHappensBefore',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymPoint']
    ),
    'PredicateFunctionSHappensBefore': GraphNode(
        'PredicateFunctionSHappensBefore',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymPoint']
    ),
    'PredicateFunctionHappensWithin': GraphNode(
        'PredicateFunctionHappensWithin',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymInterval']
    ),
    'PredicateFunctionWHappensBeforeEvent': GraphNode(
        'PredicateFunctionWHappensBeforeEvent',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymEvent']
    ),
    'PredicateFunctionSHappensBeforeEvent': GraphNode(
        'PredicateFunctionSHappensBeforeEvent',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymEvent']
    ),
    'PredicateFunctionHappensAfter': GraphNode(
        'PredicateFunctionHappensAfter',
        SUBCLASS_TYPE,
        [],
        ['SymEvent', 'SymPoint']
    ),
    'PredicateFunctionOccurs': GraphNode(
        'PredicateFunctionOccurs',
        SUBCLASS_TYPE,
        [],
        ['SymSituation', 'SymInterval']
    ),

    ## SymPoint ##
    'SymPoint': GraphNode(
        'SymPoint',
        PROP_TYPE,
        ['Point'],
        []
    ),
    'Point': GraphNode(
        'Point',
        SUBCLASS_TYPE,
        [],
        ['PointExpression'],
    ),
    'PointExpression': GraphNode(
        'PointExpression',
        PROP_TYPE,
        ['PointFunction', 'PointAtom'],
        []
    ),
    'PointFunction': GraphNode(
        'PointFunction',
        SUBCLASS_TYPE,
        [],
        ['PointAtom']
    ),
    'PointAtom': GraphNode(
        'PointAtom',
        SUBCLASS_TYPE,
        ['PointVDE', 'PointAtomObligationEvent', 'PointAtomPowerEvent', 'PointAtomContractEvent'],
        []
    ),
    'PointVDE': GraphNode(
        'PointVDE',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'PointAtomObligationEvent': GraphNode(
        'PointAtomObligationEvent',
        SUBCLASS_TYPE,
        [],
        ['ObligationEvent']
    ),
    'PointAtomPowerEvent': GraphNode(
        'PointAtomPowerEvent',
        SUBCLASS_TYPE,
        [],
        ['PowerEvent']
    ),
    'PointAtomContractEvent': GraphNode(
        'PointAtomContractEvent',
        SUBCLASS_TYPE,
        [],
        ['ContractEvent']
    ),

    ## SymInterval ##
    'SymInterval': GraphNode(
        'SymInterval',
        PROP_TYPE,
        ['Interval', 'Never'],
        []
    ),
    'Interval': GraphNode(
        'Interval',
        SUBCLASS_TYPE,
        [],
        ['IntervalExpression']
    ),
    'IntervalExpression': GraphNode(
        'IntervalExpression',
        PROP_TYPE,
        ['SituationExpression', 'IntervalFunction'],
        []
    ),
    'SituationExpression': GraphNode(
        'SituationExpression',
        SUBCLASS_TYPE,
        [],
        ['SymSituation']
    ),
    'IntervalFunction': GraphNode(
        'IntervalFunction',
        SUBCLASS_TYPE,
        [],
        ['PointExpression', 'PointExpression']
    ),

    ## SymEvent ##
    'SymEvent': GraphNode(
        'SymEvent',
        PROP_TYPE,
        ['VariableEvent', 'PowerEvent', 'ObligationEvent', 'ContractEvent'],
        []
    ),
    'VariableEvent': GraphNode(
        'VariableEvent',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'PowerEvent': GraphNode(
        'PowerEvent',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'ObligationEvent': GraphNode(
        'ObligationEvent',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'ContractEvent': GraphNode(
        'ContractEvent',
        SUBCLASS_TYPE,
        [],
        []
    ),

    ## SymSituation ##
    'SymSituation': GraphNode(
        'SymSituation',
        PROP_TYPE,
        ['ObligationState', 'PowerState', 'ContractState'],
        []
    ),
    'ObligationState': GraphNode(
        'ObligationState',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'PowerState': GraphNode(
        'PowerState',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'ContractState': GraphNode(
        'ContractState',
        SUBCLASS_TYPE,
        [],
        []
    ),
    'Never': GraphNode(
        'Never',
        SUBCLASS_TYPE,
        [],
        []
    )
}
