import re

from sympy import symbols, simplify

def validate(expr):
    return re.match(r"[-0-9xymod+*-/() ]+$", expr)

def gen(expr):
    def f(x, y):
        return eval(expr,{},{"x": x, "y": y})
    return f

def g2_associativity_check(expr):
    if not validate(expr):
        raise ValueError("Invalid expression")

    x, y, z = symbols('x y z')

    f = gen(expr)
    expr1 = f(x, f(y, z))
    expr2 = f(f(x, y), z)
    result = simplify(expr1 - expr2)

    return {
        "expr1": expr1,
        "expr2": expr2,
        "result": result
    }

if __name__ == '__main__':
    # python3 lib/g2_associativity.py 'x*y'
    # {'expr1': x*y*z, 'expr2': x*y*z, 'result': 0}
    import sys

    expr = sys.argv[1]
    result = g2_associativity_check(expr)
    print('expr1: ', result['expr1'])
    print('expr2: ', result['expr2'])
    print('diff:  ', result['result'])
