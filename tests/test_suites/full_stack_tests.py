import unittest
from typing import List
from app.src.helpers.template_getter import get_template
from app.src.grammar.selection import Selection, SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.runner import Runner

from app.templates.sample.t.nl_template import parameters

class FilledArg:
    def __init__(self, parm_key:str, selected_nodes: List[SelectedNode]):
        self.parm_key = parm_key
        self.selected_nodes = selected_nodes

# Want to have a test where we convert the sample_t into sample_raw
# Eventually I want a NL -> Node list generator... Will replace this with that..
all_args = [
    FilledArg(
        'DELIVERY_REFINEMENT',
        [
            RootNode('', 0),
            BeforeNode('', 0),
            DateNode('', 0, '2022/03/30'),
        ])
]


class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        s = 0

    @unittest.skip('in progress')
    def test_full_stack(self):
        contract = get_template('sample_t')
        expected_contract = get_template('sample_raw')
        expected_sym = expected_contract.to_sym()

        for x in all_args:
            selection = Selection.from_nodes(x.selected_nodes)
            parm_spec = parameters[x.parm_key]

            for parm_config in parm_spec.configs:
                runner = Runner(contract, parm_config)
                contract = runner.update_contract(selection)

        result = contract.to_sym()
        print(result)
        self.assertEqual(result, expected_sym)
        

if __name__ == '__main__':
    unittest.main()