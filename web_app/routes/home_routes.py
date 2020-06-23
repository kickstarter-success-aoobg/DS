from flask import Blueprint, render_template, jsonify, request
home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return "This is a test environment."

@home_routes.route("/about")
def about():
    return """This is where we build a model for prediction of Kickstarter project, 
              whether they will succeed or fail."""

my_get_list = {1: 'derp', 2: 'derpy', 3: 'derpen'}
my_post_list = {4: 'derp_post', 5: 'derpy_post', 6: 'derpen_post'}


# @home_routes.route("/predict", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         return jsonify(my_post_list)
#     else:
#         return jsonify(my_get_list)

@home_routes.route("/predict", methods=["GET", "POST"])
def predict():
    samplesub = {
        "Name": "Connor",
        "Description": "derpen",
        "Length of Campaign": 20,
        "Monetary goal": 10000,
        "Category": "derp"
        }
    if request.method == "POST":
        req = request.get_json()
        print(req)
        return samplesub, 200
        # return jsonify(my_post_list)
    else:
        return jsonify(my_get_list)