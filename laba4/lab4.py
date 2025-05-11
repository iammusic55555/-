import unittest
import math
from lab3 import radian_to_degree, degree_to_radian, compute_trig_functions

class TestTrigFunctions(unittest.TestCase):

    def test_degree_to_radian(self):
        self.assertAlmostEqual(degree_to_radian(180), math.pi, places=5)
        self.assertAlmostEqual(degree_to_radian(90), math.pi / 2, places=5)

    def test_radian_to_degree(self):
        self.assertAlmostEqual(radian_to_degree(math.pi), 180, places=5)
        self.assertAlmostEqual(radian_to_degree(math.pi / 2), 90, places=5)

    def test_compute_trig_functions_degrees(self):
        sin_value, cos_value, tan_value = compute_trig_functions(90, 'degrees', 3)
        self.assertEqual(sin_value, 1.0)
        self.assertEqual(cos_value, 0.0)
        self.assertEqual(tan_value, 'undefined')

    def test_compute_trig_functions_degrees_45(self):
        sin_value, cos_value, tan_value = compute_trig_functions(45, 'degrees', 3)
        self.assertAlmostEqual(sin_value, 0.707, places=3)
        self.assertAlmostEqual(cos_value, 0.707, places=3)
        self.assertAlmostEqual(tan_value, 1.0, places=3)

    def test_compute_trig_functions_radians(self):
        sin_value, cos_value, tan_value = compute_trig_functions(math.pi/4, 'radians', 3)
        self.assertAlmostEqual(sin_value, 0.707, places=3)
        self.assertAlmostEqual(cos_value, 0.707, places=3)
        self.assertAlmostEqual(tan_value, 1.0, places=3)

if __name__ == '__main__':
    unittest.main()