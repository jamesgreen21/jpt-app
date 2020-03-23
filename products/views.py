from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product


class ProductsListView(LoginRequiredMixin, ListView):
    """
    List view of all products available to users 
    """
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Personal Training & Products'
        context['nbar'] = 'products'
        return context


class ProductsCreateView(LoginRequiredMixin, CreateView):
    """
    Create form for adding new products
    """
    model = Product
    fields = ['name', 'description', 'price', 'image', 'product_type']

    def form_valid(self, form):
        """
        Check that form submitted is valid and save
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Update form for editing products
    """
    model = Product
    fields = ['name', 'description', 'price', 'image', 'product_type']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


# def supplier_active(request, supplier_id):
#     """
#     Check to see if the Supplier is active or deactivated and return the 
#     opposite
#     """
#     item = Suppliers.objects.get(pk=supplier_id)
#     item.is_active = False if item.is_active else True
#     item.save()
#     return redirect('suppliers')
