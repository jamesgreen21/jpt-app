from django.shortcuts import render
from django.contrib import messages


def index(request):
    """
    App home page with full detail and links for the JPT App
    Includes a user_feedback dict which would be transformed to a model
    in the second release
    """
    user_feedback = [
        {        
            'name': 'Ashleigh',
            'comments': "James is honestly a wee ray of sunshine. Not like the vast majority of pts out there trying to sell a quick fix, she’s all about empowering the body you have and encouraging body positivity. Feel amazing after my workouts with her. Great value for money and the fact she is mobile is a huge plus. Would recommend to everyone :)"
        },
        {
            'name': 'Kelly',
            'comments': "Been training with James for over two months now and can’t believe I actually look forward to our session. She knows how to push you and when to step back, cannot recommend her enough "
        },
        {
            'name': 'Robyn',
            'comments': "Been working with James for some time now and I’ve never felt so good about myself both mentally and physically. She pushes me in the nicest way possible and celebrates all my achievements which really makes me feel that bit more accomplished. I’ve never viewed fitness with such an air of positivity until I started working with James, I cannot recommend her enough to everyone; novices, those looking for a challenge and everything in between! Thank you for everything!"
        }
    ]
    context = {
        'title': 'Home',
        'nbar': 'home',
        'user_feedback': user_feedback
    }
    return render(request, 'index.html', context)


def book_a_session(request):
    """
    App Book a Session placeholder page while the Book app is under 
    development
    """
    context = {
        'title': 'Book a Session',
        'nbar': 'book',
    }
    return render(request, 'book.html', context)
