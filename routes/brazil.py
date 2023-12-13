from services.brazilData import request_brazil_covid_data
from flask import Blueprint

brazil = Blueprint("brazil", __name__)

"""
    The BrazilController is responsible for handling the requests and returning the responses.
"""


@brazil.route("/brazil", methods=['GET'])
def brazil_covid():
    return request_brazil_covid_data()
