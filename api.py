from flask import Flask
from flask.ext.restful import Resource, Api, reqparse, abort
from game import worlds, Player


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('script', type=str)


class World(Resource):

    def get_world(self, world_id):
        try:
            return worlds[world_id]
        except KeyError:
            abort(404)

    def get(self, hash):
        return self.get_world(hash).map

    def post(self, hash):

        data = parser.parse_args()
        world = self.get_world(hash)
        player = Player(world)
        script = data['script']

        try:
            # Wohooh, so naive
            # ToDo: some kind of a sandbox
            exec(script, {}, {
                'world': world,
                'guy': player,
            })
        except SyntaxError as e:
            return {'success': False, 'data': {
                "offset": e.offset,
                "lineno": e.lineno,
                "text": e.text,
                "message": e.msg
            }}, 204

        return {'success': True, 'data':{
            'steps': player.step_record
        }}, 200


api.add_resource(World, '/world/<string:hash>')


if __name__ == '__main__':
    app.run(debug=True)
