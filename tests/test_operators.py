"""Test suite for arithmetic operator behavior.

The intent of this suite is to validate calculator semantics expected by
end-users (standard arithmetic operations).
"""

import unittest

from operators import add, divide, multiply, subtract


class TestOperators(unittest.TestCase):
    """Validate operator contracts used by the calculator backend."""

    def test_add_returns_sum(self):
        """`add` should return the sum of the two operands."""
        self.assertEqual(add(2, 3), 5)

    def test_subtract_uses_left_minus_right(self):
        """`subtract` should compute `a - b` for standard subtraction."""
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply_returns_product(self):
        """`multiply` should compute `a * b` for standard multiplication."""
        self.assertEqual(multiply(4, 3), 12)

    def test_divide_returns_true_quotient(self):
        """`divide` should compute true division `a / b`."""
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero_raises(self):
        """`divide` should raise `ZeroDivisionError` when divisor is zero."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
