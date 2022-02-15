from models import create_classes
from processModel import getWineScore
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# from flask_cors import CORS
# import json
# from bson import json_util
# from flask_pymongo import PyMongo
# import collections

# Flask instance
app = Flask(__name__)

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# wineModelRed = create_classes(db, 1)
# wineModelWhite = create_classes(db, 2)

#CORS(app, support_credentials=True)
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)
# db = client.Ottawa
# construction = db.geo_
# wards = db.geo_ward

# Home route to render template
@app.route("/")
def home():

    # Return templated data
    return render_template("index.html")

@app.route("/compare")
def compare():

    # Return templated data
    return render_template("comparison.html")

@app.route("/explain")
def explain():

    # Return templated data
    return render_template("explain.html")

@app.route("/about")
def about():

    # Return templated data
    return render_template("about.html")

@app.route("/api/getwinescore", methods=["POST"])
def send():
    if request.method == "POST":       

        fixed_acidity = request.form["rng_fa"]
        volatile_acidity = request.form["rng_va"]	
        citric_acid = request.form["rng_ca"]
        residual_sugar = request.form["rng_rs"]
        chlorides = request.form["rng_c"]
        free_sulfur_dioxide = request.form["rng_fsd"]
        total_sulfur_dioxide = request.form["rng_tsd"]
        density = request.form["rng_d"]
        pH = request.form["rng_ph"]
        sulphates = request.form["rng_s"]
        alcohol = request.form["rng_a"]
        model_type = request.form["ddl_wt"]

        score = getWineScore(
            fixed_acidity, 
            volatile_acidity, 
            citric_acid, 
            residual_sugar, 
            chlorides, 
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol,
            model_type
            )     

        wine_score = [{
            "score": score
        }]

        return jsonify(wine_score)

if __name__ == "__main__":
    app.run(debug=True)