from services.brazilData import request_regions_covid_data, request_states_covid_data
from flask import Blueprint, jsonify

brazil = Blueprint("brazil", __name__)

"""
    The BrazilController is responsible for handling the requests and returning the responses.
"""


@brazil.route("/regions", methods=['GET'])
def brazil_covid_regions():
    regions_data = request_regions_covid_data()
    return jsonify(regions_data)


@brazil.route("/states", methods=['GET'])
def brazil_covid_states():
    states_data = request_states_covid_data()
    return jsonify(states_data)
