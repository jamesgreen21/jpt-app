from django.shortcuts import render
from products.models import Product
from health_blog.models import Blog, Answer
from health_blog.forms import QuestionForm


def search_blogs(request):
    blogs = Blog.objects.filter(name__icontains=request.GET['q'])
    star_answers = Answer.objects.filter(star_question=True).order_by('-created_date')
    question_form = QuestionForm()

    context = {
        'title': 'Health & Wellbeing Blog',
        'nbar': 'blog',
        'blogs': blogs,
        'question_form': question_form,
        'star_answers': star_answers,
    }

    return render(request, "blog_list.html", context)
