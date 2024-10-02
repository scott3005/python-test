
# from ..flask_server import app
# def test_main():
#     response = app.test_client().get('/')

#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'hello world'

import json
def test_main(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = 'hello world'
    assert expected == res.data.decode('utf-8')