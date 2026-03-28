# Run: python test_unittest_example.py -V
# run: python -m unittest -v test_unittest_example

import unittest


def add(x, y):
    return x + y


class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative(self):
        result = add(-1, 1)
        self.assertEqual(result, 0)

    def test_add_zero(self):
        result = add(0, 0)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
