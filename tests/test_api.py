import sys; sys.path.append('../')

import pytest


@pytest.fixture
def app():
    from api import app
    return app.test_client()


def test_get_world(app):
    response = app.get('/world/1')

    assert response.status_code == 200

