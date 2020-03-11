from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    Detail view of a single Blog Post object based on the post ID (pk) via 
    blog_detail.html Or return a 404 error if the post is not found
    """
    items = Product.objects.filter(product_type='item')
    classes = Product.objects.filter(product_type='class')
    context = {
        'title': 'Bookings',
        'nbar': 'bookings',
        'items': items,
        'classes': classes,
    }

    return render(request, "products_list.html", context)

