"""Flask entry point for the calculator web application.

This module exposes:
- the Flask application instance (`app`)
- the expression evaluator (`calculate`)
- the route handler used by the UI (`index`)
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Evaluate a binary arithmetic expression.

    Args:
        expr: Expression containing exactly two numeric operands and one
            operator among `+`, `-`, `*`, `/` (example: `12+4`).

    Returns:
        The result returned by the mapped operator function.

    Raises:
        ValueError: If the expression is empty, malformed, has multiple
            operators, or contains non-numeric operands.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Keep exactly one operator to preserve a simple "a op b" grammar.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the calculator page and process submitted expressions.

    On `GET`, this route returns the empty calculator UI.
    On `POST`, it reads the `display` form field, evaluates it with
    `calculate`, and renders either the computed value or an error message.

    Returns:
        The rendered `templates/index.html` page.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
