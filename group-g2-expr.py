import sys

from sympy import symbols, simplify

# Define the variables
x, y, z = symbols('x y z')

def gen(expr):
    def f(x, y):
        return eval(expr,{},{"x": x, "y": y})
    return f

# Compute f(a, f(b, c)) and f(f(a, b), c)
f = gen(sys.argv[1])
expr1 = f(x, f(y, z))
expr2 = f(f(x, y), z)

# Simplify the difference between the two expressions
result = simplify(expr1 - expr2)

# Print the results
print("f(x, f(y, z)) =", expr1)
print("f(f(x, y), z) =", expr2)
print("Simplified difference (expr1 - expr2) =", result)
