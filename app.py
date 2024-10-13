from flask import Flask, render_template, request

from lib import cayley, g2_associativity

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/cayley", methods=["GET"])
def cayley_handler_get():
    return render_template("cayley.html", title="Cayley")


@app.route("/cayley", methods=["POST"])
def cayley_handler_post():
    operation = request.form.get("operation")
    elements_arg = request.form.get("elements")
    elements = cayley.parse_elements_arg(elements_arg)
    table = cayley.cayley_table(elements, operation)

    result = {
        "table": table,
        "g1_closure": cayley.g1_closure(table),
        "g3_identity": cayley.g3_identity(table),
        "g4_inverses": cayley.g4_inverses(table),
    }
    return render_template(
        "cayley.html", title="Cayley", elements_arg=elements_arg, operation=operation, result=result
    )

@app.route("/g2_associativity", methods=["GET"])
def g2_associativity_handler_get():
    return render_template("g2_associativity.html", title="G2 Associativity")

@app.route("/g2_associativity", methods=["POST"])
def g2_associativity_handler_post():
    expr = request.form.get("expr")
    result = g2_associativity.g2_associativity_check(expr)
    return render_template("g2_associativity.html", title="G2 Associativity", expr=expr, result=result)
