from django.test import TestCase, Client
from .forms import BlogPostForm


class TestHealthblogBlogForm(TestCase):

    def test_pass(self):
        self.assertEqual(200, 200)
