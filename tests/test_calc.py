import unittest
from pyexample import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
