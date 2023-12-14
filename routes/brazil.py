from services.brazilData import request_regions_covid_data, request_states_covid_data
from services.citysData import city_request
from flask import Blueprint, jsonify, request

brazil = Blueprint("brazil", __name__)

"""
    The BrazilController is responsible for handling the requests and returning the responses.
"""


@brazil.route("/regions", methods=['GET'])
def regions():
    regions_data = request_regions_covid_data()
    return regions_data


@brazil.route("/states", methods=['GET'])
def states():
    states_data = request_states_covid_data()
    return jsonify(states_data)


def paginate(data, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return data[start:end]


@brazil.route("/citys", methods=['GET'])
def citys():
    citys_data = city_request('/Users/guibedan/PycharmProjects/covidData/services/data/table03.csv')

    if not citys_data:
        return jsonify({'message': 'No data available'}), 404

    page = request.args.get('page', 1, type=int)
    items_per_page = 10

    current_data = paginate(citys_data, page, items_per_page)

    total_pages = len(citys_data) // items_per_page + (len(citys_data) % items_per_page > 0)

    response = {
        'page': page,
        'total_pages': total_pages,
        'data': current_data
    }

    return jsonify(response)


@brazil.route("/citys/all", methods=['GET'])
def all_citys():
    citys_data = city_request('/Users/guibedan/PycharmProjects/covidData/services/data/table03.csv')

    if not citys_data:
        return jsonify({'message': 'No data available'}), 404

    response = {
        'data': citys_data
    }

    return jsonify(response)
