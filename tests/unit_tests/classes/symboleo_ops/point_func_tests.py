import unittest
from unittest.mock import MagicMock

from app.classes.spec.point_function import *
from app.classes.spec.sym_point import PointVDE

class PointFunctionTests(unittest.TestCase):
    def test_point_function(self):
        p = PointFunction(PointVDE('x'), 2, TimeUnit.Days)

        res = p.to_sym()

        self.assertEqual(res, 'Date.add(x, 2, days)')


    

    
  
if __name__ == '__main__':
    unittest.main()