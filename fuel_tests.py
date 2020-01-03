import unittest
from fuel_calculator import calculate_fuel


class FuelTests(unittest.TestCase):

    def test_12(self):
        self.assertEqual(calculate_fuel(12), 2)

    def test_14(self):
        self.assertEqual(calculate_fuel(14), 2)

    def test_1969(self):
        self.assertEqual(calculate_fuel(1969), 654)

    def test_100756(self):
        self.assertEqual(calculate_fuel(100756), 33583)


if __name__ == '__main__':
    unittest.main()
