import unittest
from unittest.mock import MagicMock
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.standard_event_node import CommonEventNode
from app.classes.template_event.common_event import CommonEvent

from app.src.grammar.token_processor import CommonTokenProcessor, IProcessToken
from app.src.grammar.common_event_handler import IHandleCommonEvents


class TokenProcessorTests(unittest.TestCase):
    def setUp(self):

        self.inner_processor = IProcessToken()

        self.evt_handler = IHandleCommonEvents()

        self.sut = CommonTokenProcessor(self.inner_processor, self.evt_handler)
    

    def test_token_processor_common(self):
        self.evt_handler.handle = MagicMock(return_value=SelectedNode('test'))
        self.inner_processor.process = MagicMock(return_value = None)

        sample_event = CommonEvent()
        self.sut.toggle_common(sample_event)

        token = AbstractNode()
        result = self.sut.process(token, None)

        self.assertEqual(result.value, 'test')
        self.assertEqual(self.evt_handler.handle.call_count, 1)
        self.assertEqual(self.inner_processor.process.call_count, 0)
    
    def test_token_processor_regular(self):
        self.evt_handler.handle = MagicMock(return_value=None)
        self.inner_processor.process = MagicMock(return_value = SelectedNode('test'))

        token = AbstractNode()
        result = self.sut.process(token, None)

        has_common = self.sut.has_common()

        self.assertFalse(has_common)

        self.assertEqual(result.value, 'test')
        self.assertEqual(self.evt_handler.handle.call_count, 0)
        self.assertEqual(self.inner_processor.process.call_count, 1)
    

    def test_token_processor_new_common(self):
        self.evt_handler.handle = MagicMock(return_value=None)
        self.inner_processor.process = MagicMock(return_value = CommonEventNode(CommonEvent(common_event_key='test_key')))

        token = AbstractNode()
        result = self.sut.process(token, None)

        has_common = self.sut.has_common()

        self.assertTrue(has_common)
        self.assertEqual(type(result.value), CommonEvent)
        self.assertEqual(self.evt_handler.handle.call_count, 0)
        self.assertEqual(self.inner_processor.process.call_count, 1)

    


if __name__ == '__main__':
    unittest.main()
