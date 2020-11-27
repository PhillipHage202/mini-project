from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_animal(self):
    # We will mock a response of 1 and test that we get football returned.
        with patch('requests.get') as g:
            with patch ("requests.post") as p:
                g.return_value.text = "cat"
                p.return_value.text = "meow"

<<<<<<< HEAD
            response = self.client.get(url_for('index'))
            self.assertIn(b'cat makes a noise meow', response.data)
=======
                response = self.client.get(url_for('index'))
                self.assertIn(b'cat makes  meow', response.data)
>>>>>>> 88e12f9f9c94f18e1782e8f0e5c1c5a5ae9dfa8a
