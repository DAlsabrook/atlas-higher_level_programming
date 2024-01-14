import unittest

add_integer = __import__('0-add_integer').add_integer

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add_integer(10, 5), 15)
        self.assertEqual(add_integer(1000000000000, 1), 1000000000001)
        self.assertEqual(add_integer(-10, 5), -5)
        self.assertEqual(add_integer(0, 0), 0)
        self.assertEqual(add_integer(0, "steve"), 0)

if __name__ == "__main__":
    unittest.main()
