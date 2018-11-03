import Frac
import unittest

f1 = Frac.Frac(1, 2)
f2 = Frac.Frac(-3, 8)
f3 = Frac.Frac(2, 3)
f4 = Frac.Frac(3, 7)
f5 = Frac.Frac(3, 1)
f6 = Frac.Frac(0, 2)
f7 = Frac.Frac(4, 6)


class TestFractions(unittest.TestCase):

    def test_str_frac(self):
        t1 = str(f1)
        self.assertEqual(t1, '1/2')

    def test_repr_frac(self):
        t1 = repr(f1)
        self.assertEqual(t1, 'Frac(1, 2)')

    def test_add_frac(self):
        t1 = f1 + f2
        t2 = f4 + f5
        t3 = f6 + f5
        self.assertEqual(str(t1), '1/8')
        self.assertEqual(str(t2), '24/7')
        self.assertEqual(str(t3), '6/2')

    def test_sub_frac(self):
        t1 = f3 - f4
        t2 = f4 - f5
        t3 = f6 - f5
        self.assertEqual(str(t1), '5/21')
        self.assertEqual(str(t2), '-18/7')
        self.assertEqual(str(t3), '-6/2')

    def test_mul_frac(self):
        t1 = f3 * f4
        t2 = f4 * f5
        t3 = f6 * f5
        self.assertEqual(str(t1), '6/21')
        self.assertEqual(str(t2), '9/7')
        self.assertEqual(str(t3), '0/2')

    def test_div_frac(self):
        t1 = f1 / f3
        t2 = f4 / f5
        t3 = f6 / f5
        self.assertEqual(str(t1), '3/4')
        self.assertEqual(str(t2), '3/21')
        self.assertEqual(str(t3), '0/6')

    def test_pos_frac(self):
        t1 = +f1
        self.assertEqual(str(t1), '1/2')

    def test_neg_frac(self):
        t1 = -f1
        t2 = -f6
        self.assertEqual(str(t1), '-1/2')
        self.assertEqual(str(t2), '0/2')

    def test_invert_frac(self):
        t1 = ~f1
        t2 = ~f7
        self.assertEqual(str(t1), '2')
        self.assertEqual(str(t2), '6/4')

    def test_float_frac(self):
        t1 = float(f1)
        t2 = float(f4)
        t3 = float(f6)
        t4 = float(f2)
        self.assertAlmostEqual(t1, 0.5)
        self.assertAlmostEqual(t2, 0.428571428571)
        self.assertAlmostEqual(t3, 0)
        self.assertAlmostEqual(t4, -0.375)


if __name__ == '__main__':
    unittest.main()
