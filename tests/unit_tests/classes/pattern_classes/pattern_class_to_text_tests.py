import unittest
from unittest.mock import MagicMock

from app.classes.spec.point_function import TimeUnit
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.events.base_event import BaseEvent


def mock_event():
    result = BaseEvent()
    result.to_text = MagicMock(return_value='something happens')
    return result

# TODO: Make a test suite for this functionality ... will put in test_suites
class PatternClassToTextTests(unittest.TestCase):

    def test_after_date(self):
        x = AfterDate()
        x.date_text = 'March 30, 2024'
        x.keyword = 'after'
        result = x.to_text()
        self.assertEqual(result, 'after March 30, 2024')
    

    def test_after_event(self):
        x = AfterEvent()
        x.nl_event = mock_event()
        x.keyword = 'after'
        result = x.to_text()
        self.assertEqual(result, 'after something happens')


    def test_after_timespan_after_event(self):
        x = AfterTimespanAfterEvent()
        x.nl_event = mock_event()
        x.timespan_unit = TimeUnit.Days
        x.timespan_value = 3
        x.keyword1 = 'following'
        x.keyword2 = 'after'
    
        result = x.to_text()
        self.assertEqual(result, 'following 3 days after something happens')
    
    def test_after_timespan_before_event(self):
        x = AfterTimespanBeforeEvent()
        x.nl_event = mock_event()
        x.timespan_unit = TimeUnit.Days
        x.timespan_value = 3
        x.keyword1 = 'following'
        x.keyword2 = 'before'
    
        result = x.to_text()
        self.assertEqual(result, 'following 3 days before something happens')
        

    def test_before_date(self):
        x = BeforeDate()
        x.date_text = 'March 30, 2024'
        x.keyword = 'before'
        result = x.to_text()
        self.assertEqual(result, 'before March 30, 2024')
    

    def test_before_event(self):
        x = BeforeEvent()
        x.nl_event = mock_event()
        x.keyword = 'before'
        result = x.to_text()
        self.assertEqual(result, 'before something happens')

    
    
if __name__ == '__main__':
    unittest.main()