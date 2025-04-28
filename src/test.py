import unittest
from timer import *

class TestTimerClass(unittest.TestCase):
    def test_init(self):
        t = TallyTimer()
        self.assertEqual(t.last_time, 0)
    def test_reset(self):
        t = TallyTimer()
        t.last_time = 1
        t = TallyTimer()
        self.assertEqual(t.last_time, 0)        

if __name__ == '__main__':
    unittest.main()