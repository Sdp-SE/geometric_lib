import unittest
import triangle
class TriangleTests(unittest.TestCase):
    def test_area_basic(self):
        self.assertEqual(triangle.area(4, 2), 4.0)
        self.assertEqual(triangle.area(10, 5), 25)

    def test_area_zero(self):
        self.assertEqual(triangle.area(0, 5), 0)
        self.assertEqual(triangle.area(5, 0), 0)

    def test_perimetr_basic(self):
        self.assertEqual(triangle.perimetr(3, 4, 5), 12)
        self.assertEqual(triangle.perimetr(6, 6, 6), 18)

    def test_negative_values_raise(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, 2)
        with self.assertRaises(ValueError):
            triangle.perimetr(-1, 2, 3)

    def test_invalid_types_raise(self):
        with self.assertRaises(TypeError):
            triangle.area("основание", 2)
        with self.assertRaises(TypeError):
            triangle.perimetr(1, "грань равная четырем", 3)

    def test_float_inputs(self):
        self.assertAlmostEqual(triangle.area(2.5, 4.0), 2.5 * 4.0 / 2)
        self.assertAlmostEqual(triangle.perimetr(3.5, 4.5, 5.5), 3.5 + 4.5 + 5.5)

    def test_invalid_triangle_raises(self):
        with self.assertRaises(ValueError):
            triangle.perimetr(1, 2, 10)
        with self.assertRaises(ValueError):
            triangle.perimetr(5, 1, 2)
        with self.assertRaises(ValueError):
            triangle.perimetr(1, 10, 2)

    def test_borderline_triangle_not_allowed(self):
        with self.assertRaises(ValueError):
            triangle.perimetr(3, 4, 7)
