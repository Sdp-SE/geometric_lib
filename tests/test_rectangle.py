import unittest
import rectangle

class RectangleTests(unittest.TestCase):
    def test_area_basic(self):
        self.assertEqual(rectangle.area(3, 4), 12)
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_perimetr_basic(self):
        self.assertEqual(rectangle.perimetr(3, 4), 14)
        self.assertEqual(rectangle.perimetr(0, 0), 0)

    def test_zero_side(self):
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(5, 0), 0)

    def test_float_inputs(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(rectangle.perimetr(2.5, 4.0), 2 * (2.5 + 4.0))

    def test_negative_sides_raise(self):
        with self.assertRaises(ValueError):
            rectangle.area(-2, 3)
        with self.assertRaises(ValueError):
            rectangle.perimetr(2, -3)
        with self.assertRaises(ValueError):
            rectangle.perimetr(-1, -1)

    def test_invalid_types_raise(self):
        with self.assertRaises(TypeError):
            rectangle.area("какой-то мусор", 2)
        with self.assertRaises(TypeError):
            rectangle.perimetr(1, None)

    def test_commutativity_area(self):
        self.assertEqual(rectangle.area(2, 5), rectangle.area(5, 2))

