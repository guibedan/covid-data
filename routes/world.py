from flask import Blueprint

world = Blueprint("world", __name__)

"""
    The WorldController is responsible for handling the requests and returning the responses.
"""


@world.route("/world", methods=['GET'])
def world_covid():
    return "world data"
