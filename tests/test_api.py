import sys; sys.path.append('../')

import pytest
import json

from game import worlds


@pytest.fixture
def app():
    from api import app
    return app.test_client()


def test_get_world(app):
    world_hash = '1'
    response = app.get('/world/{}'.format(world_hash))

    assert response.status_code == 200
    assert worlds[world_hash].map == json.loads(response.data.decode('utf-8'))


def test_post_script(app):
    response = app.post('/world/1', data={"script": 'print("test")'})
    assert response.status_code == 200


def test_post_script_error(app):
    response = app.post('/world/1', data={"script": 'print("test)'})
    assert response.status_code == 204
