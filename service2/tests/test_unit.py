from flask import url_for
from flask_testing import Testcase 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestAnimals(TestBase):

    def test_animal(self):
        animals = [b"cow" , b"dog", b"cat"]
        response = self.client.get(url_for('animal'))
        self.assertIn(response.data, animals)

    def test_noise_cow(self):
        response = self.client.post(
            url_for('noise'),
            data=cow,
            follow_redirects=True
        )
        self.assertIn(b'moo', response.data)
    
    def test_noise_dog(self):
        response = self.client.post(
            url_for('noise'),
            data=dog,
            follow_redirects=True
        )
        self.assertIn(b'woof', response.data)

    def test_noise_cat(self):
        response = self.client.post(
            url_for('noise'),
            data=cat,
            follow_redirects=True
        )
        self.assertIn(b'meow', response.data)