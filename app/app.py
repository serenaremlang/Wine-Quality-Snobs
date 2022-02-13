from flask import Flask, render_template, redirect, jsonify
# from flask_cors import CORS
# import json
# from bson import json_util
# from flask_pymongo import PyMongo
# import collections

# Flask instance
app = Flask(__name__)

# Mongo connection with pyMongo
# app.config["MONGO_URI"] = "mongodb://localhost:27017/Wine"
# mongo = PyMongo(app)

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


if __name__ == "__main__":
    app.run(debug=True)