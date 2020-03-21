from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Blog, Answer
from .forms import BlogPostForm, QuestionForm, AnswerForm
from accounts.models import Profile


def get_blogs(request):
    """
    Detail view of a single Blog Post object based on the post ID (pk) via 
    blog_detail.html Or return a 404 error if the post is not found
    """
    blogs = Blog.objects.order_by('-created_date')
    star_answers = Answer.objects.filter(star_question=True).order_by('-created_date')

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.instance.user = request.user
            question_form.save()
            messages.success(request, 'Your question has been sent!')
            return redirect('jpt-blogs')
    else:
        question_form = QuestionForm()

    context = {
        'title': 'Health & Wellbeing Blog',
        'nbar': 'blog',
        'blogs': blogs,
        'question_form': question_form,
        'star_answers': star_answers,
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


def create_or_edit_answers(request, pk=None):
    """
    Create a view that allows the admin to responde to the user questions
    and edit previous responses. Admin can also star messages for Q&A section
    """
    all_answers = Answer.objects.order_by('-id')
    answer = get_object_or_404(Answer, pk=pk) if pk else None
    if request.method == "POST":
        answer_form = AnswerForm(request.POST, instance=answer)
        if answer_form.is_valid():
            answer = answer_form.save()
            return redirect(create_or_edit_answers, answer.pk)
    else:
        answer_form = AnswerForm(instance=answer)

    context = {
        'title': 'Health & Wellbeing Blog',
        'nbar': 'blog',
        'edit_answer': pk,
        'answer_form': answer_form,
        'all_answers': all_answers,
    }
    return render(request, 'answer_form.html', context)


def delete_question(request, pk):
    """
    A view for deleting a question 
    """
    answer = get_object_or_404(Answer, pk=pk) if pk else None
    answer.delete()
    return redirect(create_or_edit_answers, 0)
