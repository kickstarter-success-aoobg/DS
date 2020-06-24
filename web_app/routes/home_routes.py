from flask import Blueprint, render_template, jsonify, request
home_routes = Blueprint("home_routes", __name__)
import pandas as pd
import joblib

# import pickle

# from web_app.pickled_models import baseline_pt1_nlp, baseline_pt2_rfc, categorical_encoder
# nlp = pickle.load(open("baseline_pt1_nlp.pkl", "rb"))
# rfc = pickle.load(open("baseline_pt2_rfc.pkl", "rb"))
# encode = pickle.load(open("categorical_encoder.pkl", "rb"))
nlp = joblib.load("baseline_pt1_nlp.pkl")
rfc = joblib.load("baseline_pt2_rfc.pkl")
encode = joblib.load("categorical_encoder.pkl")
    
@home_routes.route("/")
def index():
    return "This is a test environment."

@home_routes.route("/about")
def about():
    return """This is where we build a model for prediction of Kickstarter project, 
              whether they will succeed or fail."""

my_get_list = {1: 'derp', 2: 'derpy', 3: 'derpen'}
# my_post_list = {4: 'derp_post', 5: 'derpy_post', 6: 'derpen_post'}


# @home_routes.route("/predict", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         return jsonify(my_post_list)
#     else:
#         return jsonify(my_get_list)
    # # samplesub = {
    #     "Name": "Nick",
    #     "Description": "derpen",
    #     "Length of Campaign": 20,
    #     "Monetary goal": 10000,
    #     "Category": "derp"
    #     }


# @home_routes.route("/predict", methods=["GET", "POST"])
# def predict():

#     if request.method == "POST":
#         req = request.get_json()
#         print(req)
#         return { "rate" : "175.50" }, 200

#     else:
#         return jsonify(my_get_list)

@home_routes.route("/predict", methods=["GET", "POST"])
def predict():
    
    if request.method == "POST":

        req = request.get_json()
        # print(req)
        # Concatenate text inputs to prepare for NLP model
        text = req["name"] + " " + req["blurb"]

        # Generate prediction and probability of success
        prediction = nlp.predict([text])
        probability = nlp.predict_proba([text])[0][1]

        # Add probability of success to user_input
        req.update(nlp_proba = probability)

        # Remove text data
        del req['name']
        del req['blurb']

        # convert to df for categorical encoding
        req = pd.DataFrame.from_dict(req, orient='index').T

        # Encode categorical data
        req['category'] = encode.transform(req['category'])

        # Generate final prediction probability
        success_prediction = rfc.predict(req)[0]
        success_probability = rfc.predict_proba(req)[0][1]*100
        return { "success_probability" : success_probability }, 200

    else:
        samplesub = {
                    "category": "Journalism",
                    "blurb": "This is going to be THE BEST kickstarter",
                    "campaign_length": 30,
                    "usd_goal": 10000,
                    "name": "The Best Journalism Invention Ever"
                    }

        text = samplesub["name"] + " " + samplesub["blurb"]

        # Generate prediction and probability of success
        prediction = nlp.predict([text])
        probability = nlp.predict_proba([text])[0][1]

        # Add probability of success to user_input
        samplesub.update(nlp_proba = probability)

        # Remove text data
        del samplesub['name']
        del samplesub['blurb']

        # convert to df for categorical encoding
        samplesub = pd.DataFrame.from_dict(samplesub, orient='index').T

        # Encode categorical data
        samplesub['category'] = encode.transform(samplesub['category'])

        # Generate final prediction probability
        success_prediction = rfc.predict(samplesub)[0]
        success_probability = rfc.predict_proba(samplesub)[0][1]*100
        return { "success_probability" : success_probability }, 200
