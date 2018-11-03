# Kod testujący moduł.

import Point
import unittest

p1 = Point.Point(2, 1)
p2 = Point.Point(4, 8)
p3 = Point.Point(0, 3)
p4 = Point.Point(-2, 4)
p5 = Point.Point(3, -8)
p6 = Point.Point(-1, -3)
p7 = Point.Point(4, 8)


class TestPoint(unittest.TestCase):

    # def setUp(self):
    #     p1 = Point.Point(2, 1)
    #     p2 = Point.Point(4, 8)
    #     p3 = Point.Point(0, 3)
    #     p4 = Point.Point(-2, 4)
    #     p5 = Point.Point(3, -8)
    #     p6 = Point.Point(-1, -3)
    #     p7 = Point.Point(4, 8)   nie dziala?

    def test_str_point(self):
        t1 = str(p1)
        t2 = str(p4)
        self.assertEqual(t1, '(2, 1)')
        self.assertEqual(t2, '(-2, 4)')

    def test_repr_point(self):
        t1 = repr(p1)
        self.assertEqual(t1, 'Point(2, 1)')

    def test_eq_point(self):
        t1 = p1 == p2
        t2 = p2 == p7
        self.assertEqual(t1, 0)
        self.assertEqual(t2, 1)

    def test_ne_point(self):
        t1 = p1 != p2
        t2 = p2 != p7
        self.assertEqual(t1, 1)
        self.assertEqual(t2, 0)

    def test_add_point(self):
        t1 = p1 + p2
        t2 = p3 + p4
        t3 = p4 + p6
        t4 = p4 + p5
        self.assertEqual(str(t1), '(6, 9)')
        self.assertEqual(str(t2), '(-2, 7)')
        self.assertEqual(str(t3), '(-3, 1)')
        self.assertEqual(str(t4), '(1, -4)')

    def test_sub_point(self):
        t1 = p1 - p2
        t2 = p3 - p4
        t3 = p4 - p6
        t4 = p4 - p5
        self.assertEqual(str(t1), '(-2, -7)')
        self.assertEqual(str(t2), '(2, -1)')
        self.assertEqual(str(t3), '(-1, 7)')
        self.assertEqual(str(t4), '(-5, 12)')

    def test_mul_point(self):
        t1 = p1 * p2
        t2 = p3 * p4
        t3 = p4 * p6
        t4 = p4 * p5
        self.assertEqual(t1, 16)
        self.assertEqual(t2, 12)
        self.assertEqual(t3, -10)
        self.assertEqual(t4, -38)

    def test_cross_point(self):
        self.assertEqual(p1.cross(p2), 12)
        self.assertEqual(p2.cross(p3), 12)
        self.assertEqual(p4.cross(p6), 10)
        self.assertEqual(p5.cross(p6), -17)

    def test_length_point(self):
        self.assertAlmostEqual(p1.length(), 2.23606797)
        self.assertAlmostEqual(p3.length(), 3)
        self.assertAlmostEqual(p6.length(), 3.16227766016)


if __name__ == '__main__':
    unittest.main()
