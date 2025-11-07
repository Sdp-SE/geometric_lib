import unittest
import square
import rectangle

class SquareTests(unittest.TestCase):
    def test_area_basic(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(5), 25)

    def test_perimeter_basic(self):
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(5), 20)

    def test_relation_with_rectangle(self):
        for a in (0, 1, 2.5, 10):
            with self.subTest(a=a):
                self.assertEqual(square.area(a), rectangle.area(a, a))
                self.assertEqual(square.perimeter(a), rectangle.perimetr(a, a))

    def test_negative_side_raises(self):
        with self.assertRaises(ValueError):
            square.area(-3)
        with self.assertRaises(ValueError):
            square.perimeter(-3)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            square.area("не число, 1234")
        with self.assertRaises(TypeError):
            square.perimeter(None)

