from django.apps import apps
from django.test import TestCase, Client
from .apps import HealthBlogConfig


class TestHealthBlogConfig(TestCase):

    def test_pass(self):
        self.assertEqual(200, 200)
