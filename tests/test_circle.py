import math
import unittest
import circle

class CircleTests(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_positive_ints(self):
        self.assertAlmostEqual(circle.area(1), math.pi)
        self.assertAlmostEqual(circle.area(2), math.pi * 4)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)

    def test_area_float_precision(self):
        r = 0.123
        self.assertAlmostEqual(circle.area(r), math.pi * r * r)

    def test_large_values(self):
        r = 10**6
        self.assertAlmostEqual(circle.area(r), math.pi * r * r)
        self.assertAlmostEqual(circle.perimeter(r), 2 * math.pi * r)

    def test_negative_radius_raises_value_error(self):
        with self.assertRaises(ValueError):
            circle.area(-1)
        with self.assertRaises(ValueError):
            circle.perimeter(-0.0001)

    def test_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            circle.area("не число")
        with self.assertRaises(TypeError):
            circle.perimeter(None)


