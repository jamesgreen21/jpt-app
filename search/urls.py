from django.urls import path
from .views import search_blogs


urlpatterns = [
    path('health-and-wellbeing-blog/', search_blogs, name='search')
]
