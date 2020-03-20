from django.urls import path
from .views import (
                    get_blogs,
                    blog_detail,
                    create_or_edit_blog,
                    delete_blog,
                    create_or_edit_answers,
                    delete_question
                   )


urlpatterns = [
    path('', get_blogs, name='jpt-blogs'),
    path('<int:pk>/', blog_detail, name='view-blog'),
    path('new/', create_or_edit_blog, name='new-blog'),
    path('edit/<int:pk>/', create_or_edit_blog, name='edit-blog'),
    path('delete/<int:pk>/', delete_blog, name='delete-blog'),
    path('questions/<int:pk>/', create_or_edit_answers, name='blog_questions'),
    path('questions/delete/<int:pk>/', delete_question, name='delete_question'),
]
