from flask import Blueprint, jsonify
from services.brazil import BrazilService

brazil = Blueprint("brazil", __name__)

"""
    The BrazilController is responsible for handling the requests and returning the responses.
"""


@brazil.route("/brazil/regions", methods=['GET'])
def regions():
    regions_data = BrazilService().get_regions()
    return jsonify(regions_data)


@brazil.route("/brazil/states", methods=['GET'])
def states():
    states_data = BrazilService().get_states()
    return jsonify(states_data)


def paginate(data, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return data[start:end]


@brazil.route("/brazil/cities/<page>", methods=['GET'])
def cities(page: int):

    page = int(page) if page else 1

    citys_data = BrazilService().get_cities(page)

    if not citys_data:
        return jsonify({'message': 'No data_cities available'}), 404

    response = {
        'page': page,
        'data_cities': citys_data
    }

    return jsonify(response)


@brazil.route("/brazil/cities/all", methods=['GET'])
def all_cities():
    citys_data = BrazilService().get_cities()

    if not citys_data:
        return jsonify({'message': 'No data_cities available'}), 404

    response = {
        'data_cities': citys_data
    }

    return jsonify(response)
