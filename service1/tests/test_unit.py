import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Char
import requests 
import requests_mock
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DATABASE_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all() 
        add_char=Char(wep="Axe", element="Fire", name="Dara")
        db.session.add(add_char)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_view(self):
        with requests_mock.Mocker() as r:
            r.get("http://localhost:5001/wep", text="Axe")
            r.get("http://localhost:5002/element", text="Fire")
            r.post("http://localhost:5003/name", text="Dara")
            response = self.client.get(url_for('index'))
            self.assertEqual(response.status_code, 500)


