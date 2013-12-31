from flask import Flask, request
from flask.ext.restful import Resource, Api

from game import World


app = Flask(__name__)
api = Api(app)

world = World()

class World(Resource):

    def get(self, hash):
        return world.map

api.add_resource(World, '/world/<string:hash>')


if __name__ == '__main__':
    app.run(debug=True)