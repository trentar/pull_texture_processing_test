import unittest

# Logic to test
def calculate_total(price, tax_rate, discount=0):
    if price < 0 or tax_rate < 0 or discount < 0:
        raise ValueError("Values cannot be negative")
    return (price - discount) * (1 + tax_rate)


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.standard_tax = 0.05
        self.luxury_tax = 0.20

    def test_calculate_total_standard(self):
        result = calculate_total(100, self.standard_tax)
        self.assertEqual(result, 105.0)

    def test_calculate_total_with_discount(self):
        result = calculate_total(100, self.standard_tax, discount=10)
        self.assertEqual(result, 94.5)

    def test_negative_inputs_raise_value_error(self):
        with self.assertRaises(ValueError):
            calculate_total(-100, self.standard_tax)

    def test_zero_values(self):
        result = calculate_total(0, 0)
        self.assertEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()