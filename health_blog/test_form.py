from django.shortcuts import render, redirect, get_object_or_404
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django import forms
from .models import Blog, Question, Answer
from .forms import BlogPostForm


class TestHealthblogBlogForm(TestCase):

    def test_pass(self):
        self.assertEqual(200, 200)
