from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Blog(models.Model):
    """
    A single Blog post for the Health & Wellbeing Blogs section
    """
    title = models.CharField(max_length=50, unique=True)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_img')
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    content_image = models.ImageField(upload_to='blog_img')
    instructions = models.TextField(null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    A single Question post for the Health & Wellbeing Blogs section
    Allows customers to post questions
    """
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        form.save_m2m()
        return instance


class Answer(models.Model):
    """
    A single Answer post for the Health & Wellbeing Blogs section
    Allows admin to post answers
    """
    content = models.CharField(max_length=200, default='Awaiting Response')
    created_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    star_question = models.BooleanField(default=False)

    def __str__(self):
        return self.content
