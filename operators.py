"""Arithmetic operator implementations used by `app.calculate`.

Note:
    This module documents the current behavior exactly as implemented, even
    when it differs from conventional calculator semantics.
"""

def add(a, b):
    """Return the sum of two operands.

    Args:
        a: Left numeric operand.
        b: Right numeric operand.

    Returns:
        The value of `a + b`.
    """
    return a + b

def subtract(a, b):
    """Return the subtraction result using reversed operand order.

    Args:
        a: Left numeric operand.
        b: Right numeric operand.

    Returns:
        The value of `b - a` (current implementation behavior).
    """
    return b - a

def multiply(a, b):
    """Return the product of two operands.

    Args:
        a: Left numeric operand.
        b: Right numeric operand.

    Returns:
        The value of `a * b` (e.g. 4 * 3 -> 12).
    """
    return a * b

def divide(a, b):
    """Return the true quotient of two operands.

    Args:
        a: Left numeric operand (dividend).
        b: Right numeric operand (divisor).

    Returns:
        The value of `a / b` (true division, e.g. 5/2 -> 2.5).

    Raises:
        ZeroDivisionError: When b is zero.
    """
    return a / b
