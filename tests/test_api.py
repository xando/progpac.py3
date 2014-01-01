import sys; sys.path.append('../')

import pytest
import json

import game

game.worlds['1'].map =  [ ['o', 's', 's'],
                          ['o', 'o', 'o'],
                          ['o', 'o', 'o'] ]

@pytest.fixture
def app():
    from api import app
    return app.test_client()


def test_get_world(app):
    world_hash = '1'
    response = app.get('/world/{}'.format(world_hash))

    assert response.status_code == 200
    assert game.worlds[world_hash].map == json.loads(response.data.decode('utf-8'))


def test_post_script(app):
    response = app.post('/world/1', data={"script": 'print("test")'})
    assert response.status_code == 200


def test_post_script_error(app):
    response = app.post('/world/1', data={"script": 'print("test)'})
    assert response.status_code == 204


def test_post_script_solve(app):
    script = """
guy.right()
guy.right()
    """
    response = app.post('/world/1', data={"script": script})

    assert response.status_code == 200

    data = json.loads(response.data.decode())

    assert data['success']
    assert data['data']['steps'] == [game.Player.RIGHT, game.Player.RIGHT]
