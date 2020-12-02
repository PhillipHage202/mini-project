import requests
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class Test_view(TestBase):
    def test__element_view(self):
        response = self.client.get(url_for('element'))
        self.assertEquals(response.status_code,200)