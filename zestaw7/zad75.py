import unittest
import Circle as circ
from math import pi

f1 = circ.Circle(1, 1, 5)
f2 = circ.Circle(0, 0, 1)
f3 = circ.Circle(-4, 2, 7)
f4 = circ.Circle(5, 7, 2)


class TestCircle(unittest.TestCase):

    def test_repr_circle(self):
        self.assertEqual(repr(f1), 'Circle(1,1,5)')

    def test_eq_circle(self):
        self.assertEqual(f1 == circ.Circle(1, 1, 5), True)
        self.assertEqual(f1 == f2, False)

    def test_ne_circle(self):
        self.assertEqual(f1 != circ.Circle(1, 1, 5), False)
        self.assertEqual(f1 != f2, True)

    def test_area_circle(self):
        self.assertAlmostEqual(f1.area(), 78.539816339)
        self.assertAlmostEqual(f2.area(), pi)

    def test_move_circle(self):
        self.assertEqual(repr(f1.move(3, -3)), 'Circle(4,-2,5)')

    def test_cover_circle(self):
        self.assertEqual(repr(f1.cover(f4)), 'Circle(2.1679497056621564,2.7519245584932337,7.105551275463989)')

    def test_exceptions_circle(self):
        self.assertRaises(ValueError, circ.Circle, -2, -2, -1)
        self.assertRaises(ValueError, circ.Circle, -2, "a", -1)
        self.assertRaises(ValueError, circ.Circle, "a", -2, -1)


if __name__ == '__main__':
    unittest.main()
