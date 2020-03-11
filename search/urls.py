from django.urls import path
from .views import search_product


urlpatterns = [
    path('', search_product, name='search')
]
