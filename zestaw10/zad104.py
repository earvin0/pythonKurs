import unittest
import Queue as q


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.queue = q.Queue(5)

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.put(2)
        self.assertEqual(self.queue.is_empty(), False)

    def test_is_full(self):
        self.assertEqual(self.queue.is_full(), False)
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(3)
        self.queue.put(4)
        self.queue.put(5)
        self.assertEqual(self.queue.is_full(), True)

    def test_put(self):
        self.queue.put(5)
        self.queue.put(2)
        self.assertEqual(self.queue.items[0], 5)
        self.assertEqual(self.queue.items[1], 2)
        self.assertEqual(self.queue.items[2], None)
        self.queue.put(2)
        self.queue.put(2)
        self.queue.put(2)
        with self.assertRaises(ValueError):
            self.queue.put(2)

    def test_get(self):
        self.queue.put(1)
        self.queue.put(2)
        self.assertEqual(self.queue.get(), 1)
        self.assertEqual(self.queue.get(), 2)
        with self.assertRaises(ValueError):
            self.queue.get()


if __name__ == '__main__':
    unittest.main()
