from flask import url_for
from flask_testing import Testcase 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
'''
class TestAnimals(TestBase):

    def test_animals(self):
        animals = [b"cow",b"dog",b"cat"]
        response = self.client.get(url_for('animal'))
        self.assertIn(response.data, animals)

    def test_noise_lion(self):
        response = self.client.post(
            url_for('noise'
            data=cow)
        )
    '''