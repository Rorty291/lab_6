import unittest

from src.simple_timer.display import display_countdown
from src.simple_timer.timer import start_timer

class TestLab6(unittest.TestCase):

    def test_display(self):
        self.assertEqual(display_countdown(1), 1)

    def test_start_time(self):
        self.assertEqual(start_timer(1), True)


if __name__ == '__main__':
    unittest.main()