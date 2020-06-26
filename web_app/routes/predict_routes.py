
from flask import Blueprint, render_template, jsonify, request
import pandas as pd
import joblib

predict_routes = Blueprint("predict_routes", __name__)

nlp = joblib.load("baseline_pt1_nlp.pkl")
rfc = joblib.load("baseline_pt2_rfc.pkl")
encode = joblib.load("categorical_encoder.pkl")


@predict_routes.route("/predictor", methods=["GET", "POST"])
def predict():
    '''
    Generate prediction in percentage for user_input
    '''
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