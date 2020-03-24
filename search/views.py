from django.shortcuts import render
from products.models import Product
from health_blog.models import Question
from health_blog.forms import QuestionForm


def search_questions(request):
    questions = Question.objects.filter(content__icontains=request.GET['q'])

    context = {
        'title': 'Health & Wellbeing Blog',
        'nbar': 'blog',
        'questions': questions,
    }

    return render(request, "answer_detail.html", context)
