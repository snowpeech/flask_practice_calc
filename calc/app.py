# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/<operator>')
def maths(operator):
    a=int(request.args["a"])
    b=int(request.args["b"])
    
    if operator=="add":
        return str(add(a,b))

    elif operator=="sub":
        return str(sub(a,b))

    elif operator=="mult":
        return str(mult(a,b))

    elif operator=="div":
        return str(div(a,b))

# @app.route("/math/<operator>")
# def routing(operator):
#     if operator=="add":
#         return "add"
#
#     elif operator=="sub":
#         return "sub"
#
#     elif operator=="mult":
#         return "mult"
#
#     elif operator=="div":
#         return "div"
#