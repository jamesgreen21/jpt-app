from django.urls import path
from .views import search_questions


urlpatterns = [
    path('health-and-wellbeing-blog/', search_questions, name='search')
]
