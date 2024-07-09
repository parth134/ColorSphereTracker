import unittest
from ball_tracking import determine_quadrant

class TestBallTracking(unittest.TestCase):
    def test_determine_quadrant(self):
        self.assertEqual(determine_quadrant(10, 10, 50, 50, 100, 100), 1)
        self.assertEqual(determine_quadrant(60, 10, 50, 50, 100, 100), 2)
        self.assertEqual(determine_quadrant(10, 60, 50, 50, 100, 100), 3)
        self.assertEqual(determine_quadrant(60, 60, 50, 50, 100, 100), 4)

if __name__ == '__main__':
    unittest.main()
