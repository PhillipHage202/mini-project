from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app

class TestViews(TestCase):
    def test_homepage_view(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

class TestResponse(TestBase):
    def test_page(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "Fire"
                p.return_value.text = "Jell"

                response = self.client.get(url_for("index"))
                self.assertEqual(response.status_code, 200)