from flask import Blueprint, jsonify

from services.world import WorldService

world = Blueprint("world", __name__)

"""
    The WorldController is responsible for handling the requests and returning the responses.
"""


@world.route("/world", methods=['GET'])
def world_covid():
    world_data = WorldService().get_world()
    return jsonify(world_data)
