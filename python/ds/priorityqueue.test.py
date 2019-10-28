import unittest
import priorityqueue

class PriorityQueueTest(unittest.TestCase):

    def test_empty(self):
        q = PriorityQueue(None)
        self.assertTrue(q.is_empty())

if __name__ == '__main__':
    unittest.main()
