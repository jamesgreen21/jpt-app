from django.test import TestCase, Client
from .models import Blog
import datetime


class TestBlogModel(TestCase):

    def test_pass(self):
        self.assertEqual(200, 200)
