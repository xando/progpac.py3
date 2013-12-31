from flask import Flask, request, abort
from flask.ext.restful import Resource, Api

from game import worlds


app = Flask(__name__)
api = Api(app)

class World(Resource):

    def get(self, hash):
        try:
            return worlds[hash]().map
        except KeyError:
            abort(404)


api.add_resource(World, '/world/<string:hash>')


if __name__ == '__main__':
    app.run(debug=True)
