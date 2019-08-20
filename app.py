import os

import pandas as pd
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///static/sql/gun_violence.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Guns = Base.classes.gun_violence

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/plots/sunburst")
def sunburst():
    """Goto the data page."""
    return render_template("sunburst.html")

@app.route("/plots/mass_map")
def mass_map():
    """Goto the data page."""
    return render_template("mass_map.html")

@app.route("/plots/cluster_map")
def cluster_map():
    """Goto the data page."""
    return render_template("cluster_map.html")

@app.route("/comparisons")
def comparisons():
    """Goto the data page."""
    return render_template("comparisons.html")

@app.route("/data/")
def data():
    """Goto the data page."""
    return render_template("data.html")

@app.route("/api/v1.0/gun_violence")
def gun_violence():

    data_query = session.query(Guns.ID, Guns.Type, Guns.Gender, Guns.LegalWeapons, Guns.MentalHealthIssues, Guns.Location, Guns.Race, Guns.Latitude, Guns.Longitude, Guns.Total_Victims).all()

    all_data = []
    for ID, Type, Gender, LegalWeapons, MentalHealthIssues, Location, Race, Latitude, Longitude, Total_Victims in data_query:
        gun_dict = {}
        gun_dict["ID"] = ID
        gun_dict["Type"] = Type
        gun_dict["Gender"] = Gender
        gun_dict["LegalWeapons"] = LegalWeapons
        gun_dict["MentalHealthIssues"] = MentalHealthIssues
        gun_dict["Location"] = Location
        gun_dict["Race"] = Race
        gun_dict["Latitude"] = Latitude
        gun_dict["Longitude"] = Longitude
        gun_dict["Total_Victims"] = Total_Victims

        all_data.append(gun_dict)

    return jsonify(all_data)


if __name__ == "__main__":
    app.run()