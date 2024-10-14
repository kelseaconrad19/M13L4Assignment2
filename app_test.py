import unittest
from application.app import my_app as app

class TestApp(unittest.TestCase):
    def test_negative_sum(self):
        result = -5 + -3
        self.assertEqual(result, -8, "The sum of -5 and -3 should be -8")

if __name__ == '__main__':
    unittest.main()
