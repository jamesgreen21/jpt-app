from django.apps import apps
from django.test import TestCase
from .apps import HealthBlogConfig


class TestHealthBlogConfig(TestCase):

    def test_app(self):
        self.assertEqual("health_blog", HealthBlogConfig.name)
        self.assertEqual("health_blog", apps.get_app_config("health_blog").name)