from django.test import TestCase, Client
from django.shortcuts import get_object_or_404, reverse
import datetime
from .models import Blog


class TestViews(TestCase):

    def test_pass(self):
        self.assertEqual(200, 200)
