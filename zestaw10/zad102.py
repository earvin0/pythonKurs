import unittest
import Stack as s


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.stack = s.Stack(5)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(3)
        self.stack.push(3)
        self.assertEqual(self.stack.is_empty(), False)

    def test_is_full(self):
        self.assertEqual(self.stack.is_full(), False)
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(self.stack.is_full(), True)

    def test_push(self):
        self.stack.push(5)
        self.stack.push(2)
        self.assertEqual(self.stack.items[0], 5)
        self.assertEqual(self.stack.items[1], 2)
        self.assertEqual(self.stack.items[2], None)
        self.stack.push(5)
        self.stack.push(2)
        self.stack.push(5)
        with self.assertRaises(ValueError):
            self.stack.push(2)

    def test_pop(self):
        self.stack.push(5)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 5)
        with self.assertRaises(ValueError):
            self.stack.pop()


if __name__ == '__main__':
    unittest.main()
