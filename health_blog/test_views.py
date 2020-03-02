from django.test import TestCase
from django.shortcuts import get_object_or_404, reverse
from .models import Blog


class TestViews(TestCase):

    def test_get_blog_list_page(self):
        page = self.client.get("/health-and-wellbeing-blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog_list.html")

    def test_get_new_blog_page(self):
        page = self.client.get("/health-and-wellbeing-blog/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog_form.html")

    def test_get_edit_blog_page(self):
        blog = Blog(
            title = 'Create Test',
            headline = 'This is a Test',
            content = 'Just a test',
        )
        blog.save()

        page = self.client.get("/health-and-wellbeing-blog/edit/{0}/".format(blog.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog_form.html")

    def test_get_edit_blog_page_for_blog_that_does_not_exist(self):
        page = self.client.get("/health-and-wellbeing-blog/edit/1/")
        self.assertEqual(page.status_code, 404)

    def test_post_create_a_blog(self):
        response = self.client.post("/health-and-wellbeing-blog/new/", {
            'title': 'Create Test',
            'headline': 'This is a Test',
            'content': 'Just a test',
        })
        blog = get_object_or_404(Blog, pk=1)
        self.assertEqual(blog.views, 0)

    def test_post_edit_a_blog(self):
        blog = Blog(
            title = 'Create Test',
            headline = 'This is a Test',
            content = 'Just a test',
        )
        blog.save()
        id = blog.id
        response = self.client.post(
            "/health-and-wellbeing-blog/edit/{0}/".format(id),
            {
                "title": "Create Test Updated",
                'headline': 'This is a Test',
                'content': 'Just a test',
            }
        )
        blog = get_object_or_404(Blog, pk=id)
        self.assertEqual('Create Test Updated', blog.title)

    def test_get_blog_detail_page(self):
        blog = Blog(
            title = 'Create Test',
            headline = 'This is a Test',
            content = 'Just a test',
        )
        blog.save()
        id = blog.id
        page = self.client.get("/health-and-wellbeing-blog/{0}/".format(id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog_detail.html")

    def test_delete_a_blog(self):
        blog = Blog(
            title = 'Create Test',
            headline = 'This is a Test',
            content = 'Just a test',
        )
        blog.save()
        id = blog.id
        response = self.client.post("/health-and-wellbeing-blog/delete/{0}/".format(id))
        self.assertRedirects(response, '/health-and-wellbeing-blog/', status_code=302)
