import fracs
import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]   #przed testami

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([-1, 2], [1, 3]), [-1, 6])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.sub_frac([10, 20], [5, 8]), [-5, 40])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 2], [3, 4]), [3, 8])
        self.assertEqual(fracs.mul_frac([-2, 2], [3, 4]), [-6, 8])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([0, 2], [3, 3]), [0, 6])
        self.assertEqual(fracs.div_frac([3, 2], [-4, 3]), [9, -8])

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive([2, 2]))
        self.assertTrue(fracs.is_positive([-5, -4]))
        self.assertFalse(fracs.is_positive([30, -4]))
        self.assertFalse(fracs.is_positive([-4, 3]))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero([0, 3]))
        self.assertFalse(fracs.is_zero([-2, 2]))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([3, 2], [-4, 3]), 1)
        self.assertEqual(fracs.cmp_frac([2, 3], [3, 4]), -1)
        self.assertEqual(fracs.cmp_frac([2, 3], [4, 6]), 0)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([0, 3]), 0)
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(fracs.frac2float([2, 3]), 0.66666666)

    def tearDown(self): pass   #tutaj nie ma co sprzatac


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy