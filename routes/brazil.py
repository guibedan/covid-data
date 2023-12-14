from flask import Blueprint, jsonify, request

from services.regions import RegionsService
from services.states import StatesService
from services.cities import CitiesService

brazil = Blueprint("brazil", __name__)

"""
    The BrazilController is responsible for handling the requests and returning the responses.
"""


@brazil.route("/regions", methods=['GET'])
def regions():
    regions_data = RegionsService().get_regions()
    return regions_data


@brazil.route("/states", methods=['GET'])
def states():
    states_data = StatesService().get_states()
    return jsonify(states_data)


def paginate(data, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return data[start:end]


@brazil.route("/citys", methods=['GET'])
def citys():
    citys_data = CitiesService().get_cities()

    if not citys_data:
        return jsonify({'message': 'No data_cities available'}), 404

    page = request.args.get('page', 1, type=int)
    items_per_page = 10

    current_data = paginate(citys_data, page, items_per_page)

    total_pages = len(citys_data) // items_per_page + (len(citys_data) % items_per_page > 0)

    response = {
        'page': page,
        'total_pages': total_pages,
        'data_cities': current_data
    }

    return jsonify(response)


@brazil.route("/citys/all", methods=['GET'])
def all_citys():
    citys_data = CitiesService().get_cities()

    if not citys_data:
        return jsonify({'message': 'No data_cities available'}), 404

    response = {
        'data_cities': citys_data
    }

    return jsonify(response)
