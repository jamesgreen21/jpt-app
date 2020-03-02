from django.test import TestCase
from .forms import BlogPostForm


class TestHealthblogBlogForm(TestCase):

    def test_can_create_a_blog_with_required_fields(self):
        form = BlogPostForm({
            'title': 'Create Test',
            'headline': 'This is a Test',
            'content': 'Just a test',
        })
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_title(self):
        form = BlogPostForm({
            'title': '',
            'headline': 'This is a Test',
            'content': 'Just a test',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
