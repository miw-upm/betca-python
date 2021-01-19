from http import HTTPStatus
from unittest import TestCase

from fastapi.testclient import TestClient

from rest.dtos import Dto
from rest.main import app

client = TestClient(app)


class TestService(TestCase):
    def test_read_basic(self):
        response = client.get("/basic/666")
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual('666', response.json()['id'])
        self.assertEqual({'id': '666', 'name': 'dto', 'description': 'desc', 'value': None}, response.json())
        print('response: ', response.json())

    def test_create(self):
        response = client.post("/basic", json=Dto(id='1', name="dto", description='desc').dict())
        self.assertEqual(HTTPStatus.OK, response.status_code)
        print(response.json())

    def test_update(self):
        response = client.put("/basic/666", json={'id': '666', 'name': 'dto', 'description': 'desc'})
        self.assertEqual(HTTPStatus.OK, response.status_code)
        print(response.json())

    def test_delete(self):
        response = client.delete("/basic/666")
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_read_auth(self):
        response = client.get("/auth/basic-beginning", auth=('jes', 'pass'))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        print(response.json())

    def test_read_auth_ok(self):
        response = client.get("/auth/basic", auth=('jes', 'pass'))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        print(response.json())

    def test_read_auth_error(self):
        response = client.get("/auth/basic", auth=('jes', 'passs'))
        self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)

    def test_create_token_and_get(self):
        response = client.post("/auth/bearer", auth=('jes', 'pass'))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        token = response.json()['token']
        print(token)
        response = client.get("/auth/bearer", headers={"Authorization": "Bearer " + token})
        self.assertEqual(HTTPStatus.OK, response.status_code)
        print(response.json())

    def test_get_token_expired(self):
        bearer = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqZXMiLCJleHAiOjE2MTA0Nzg3NjV9" \
                ".afan2BHHqn14mOuGRWcNcPrkbObVm_aBGmn4IbYwXQQ"
        response = client.get("/auth/bearer", headers={"Authorization": bearer})
        self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)
