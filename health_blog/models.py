from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Blog(models.Model):
    """
    A single Blog post for the Health & Wellbeing Blogs section
    Creates a slug of the title for navigation
    """
    title = models.CharField(max_length=50, unique=True)
    headline = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        upload_to='blog_img',
        default='blog_img/default.jpg',
    )
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
