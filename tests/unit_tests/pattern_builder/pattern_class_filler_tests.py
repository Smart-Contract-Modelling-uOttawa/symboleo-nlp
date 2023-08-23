import unittest
from unittest.mock import MagicMock

from app.classes.operations.user_input import UserInput, UnitType
from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.src.pattern_builder.pattern_class_filler import PatternClassFiller, IFillPatternUnit
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import DefaultPatternFiller

class PatternClassFillerTests(unittest.TestCase):
    def setUp(self):
        self.fake_filler = IFillPatternUnit()
        d = {
            UnitType.DUMMY: self.fake_filler
        } 

        self.sut = PatternClassFiller(d)

    def test_pattern_filler(self):
        fake_pc = PatternClass(val_dict={
            PV.AND: 'test'
        })
        self.fake_filler.fill = MagicMock(return_value=fake_pc)

        fake_pc = PatternClass()
        input_list = [
            UserInput(UnitType.DUMMY, 'x'),
            UserInput(UnitType.DUMMY, 'x')
        ]

        result = self.sut.fill(fake_pc, None, input_list)

        self.assertEqual(result.val_dict[PV.AND], 'test')
        self.assertEqual(self.fake_filler.fill.call_count, 2)
    
    def test_default_pattern_filler(self):
        fake_pc = PatternClass(val_dict={
            PV.AND: 'test'
        })

        sut = DefaultPatternFiller()

        result = sut.fill(fake_pc, None, [], 0)
        
        self.assertEqual(result.val_dict[PV.AND], 'test')

        

if __name__ == '__main__':
    unittest.main()
