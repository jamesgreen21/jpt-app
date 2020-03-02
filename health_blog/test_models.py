from django.test import TestCase
from .models import Blog
import datetime


class TestBlogModel(TestCase):

    def test_views_defaults_to_zero(self):
        blog = Blog(
            title = 'Create Test',
            headline = 'This is a Test',
            content = 'Just a test',
        )
        blog.save()
        self.assertEqual(blog.title, 'Create Test')
        self.assertFalse(blog.views)

    def test_can_create_a_blog_with_required_fields_and_views_equal_two(self):
        blog = Blog(
            title = 'Create Test',
            headline = 'This is a Test',
            content = 'Just a test',
            views = 2
        )
        blog.save()
        self.assertEqual(blog.title, 'Create Test')
        self.assertEqual(blog.views, 2)
    
    def test_the_created_date_field_contains_todays_date(self):
        blog = Blog(
            title = 'Create Test',
            headline = 'This is a Test',
            content = 'Just a test',
        )
        blog.save()
        self.assertEqual(blog.created_date.date(), datetime.datetime.now().date())

    def test_blog_as_a_string(self):
        blog = Blog(title = 'Create Test')
        self.assertEqual('Create Test', str(blog))
   