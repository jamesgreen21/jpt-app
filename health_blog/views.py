from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogPostForm


def get_blogs(request):
    """
    Detail view of a single Blog Post object based on the post ID (pk) via 
    blog_detail.html Or return a 404 error if the post is not found
    """
    blogs = Blog.objects.order_by('-created_date')
    context = {
        'title': 'Health & Wellbeing Blog',
        'nbar': 'blog',
        'blogs': blogs
    }

    return render(request, "blog_list.html", context)


def blog_detail(request, pk):
    """
    Detail view of a single Blog Post object based on the post ID (pk) via 
    blog_detail.html Or return a 404 error if the post is not found
    """
    blog = get_object_or_404(Blog, pk=pk)
    blog.views += 1
    blog.save()
    context = {
        'title': blog.title,
        'nbar': 'blog',
        'blog': blog
    }

    return render(request, "blog_detail.html", context)


def create_or_edit_blog(request, pk=None):
    """
    Create a view that allows the user to create or edit Blogs via 
    blogs_form.html depending if the Blog ID is null or not
    """
    blog = get_object_or_404(Blog, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect(blog_detail, blog.pk)
    else:
        form = BlogPostForm(instance=blog)

    context = {
        'title': 'Health & Wellbeing Blog',
        'nbar': 'blog',
        'form': form,
        'blog': blog,
    }

    return render(request, 'blog_form.html', context)


def delete_blog(request, pk):
    """
    A view for deleting a blog 
    """
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect(get_blogs)
