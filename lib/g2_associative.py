from sympy import symbols, simplify

def gen(expr):
    def f(x, y):
        return eval(expr,{},{"x": x, "y": y})
    return f

def g2_associative_check(expr):
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
