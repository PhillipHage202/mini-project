from flask import url_for
from flask_testing import Testcase 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_fortune_view(self):
        with requests_mock.Mocker() as r:
            r.get("http://service2:5001/fortune/colour", text="blue")
            r.get("http://service3:5002/fortune/number", text="1")
            r.post("http://service4:5003/fortune/fortune", text="We do not know the future, but have a cookie.")
            response = self.client.get(url_for('fortune'))
            self.assertEqual(response.status_code, 200)