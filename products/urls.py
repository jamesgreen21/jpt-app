from django.urls import path
from .views import (
                    ProductsListView,
                    ProductsCreateView,
                    ProductsUpdateView,
                   )
from . import views

urlpatterns = [
    path('', ProductsListView.as_view(), name='products'),
    path('new/', ProductsCreateView.as_view(), name='new-product'),
    path('edit/<int:pk>/', ProductsUpdateView.as_view(), name='edit-product'),
]
