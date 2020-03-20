from django.contrib import admin
from .models import Blog, Question, Answer


admin.site.register([Blog, Question, Answer])
