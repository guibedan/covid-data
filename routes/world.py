from flask import Blueprint, jsonify

from services.worldData import world_request

world = Blueprint("world", __name__)

"""
    The WorldController is responsible for handling the requests and returning the responses.
"""


@world.route("/world", methods=['GET'])
def world_covid():
    world_data = world_request()
    return jsonify(world_data)
