from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app



class TestResponse(TestBase):
    def test_view(self):
        with requests_mock.Mocker() as r:
            r.get("http://localhost:5001/wep", text="Axe")
            r.get("http://localhost:5002/element", text="fire")
            r.post("http://localhost:5003/name", text="Jell")
            response = self.client.get(url_for('index'))
            self.assertEqual(response.status_code, 500)


