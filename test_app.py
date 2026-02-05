import unittest
from app import add, divide

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 0), 0)  # ❌ This will fail

if __name__ == "__main__":
    unittest.main()
