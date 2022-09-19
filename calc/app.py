from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


# @app.route('/add')
# def add_func():
#   """ Add a and b """

#   a = int(request.args["a"])
#   b = int(request.args["b"])
#   return str(add(a,b))


# @app.route('/sub')
# def sub_func():
#   """ Subtract a and b """

#   a = int(request.args["a"])
#   b = int(request.args["b"])
#   return str(sub(a,b))


# @app.route('/mult')
# def mult_func():
#   """ Multiply a and b """

#   a = int(request.args["a"])
#   b = int(request.args["b"])
#   return str(mult(a,b))


# @app.route('/div')
# def div_func():
#   """ Divide a and b """

#   a = int(request.args["a"])
#   b = int(request.args["b"])
#   return str(div(a,b))



# Springboard's more condensed version

# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)