from django.shortcuts import render


def index(request):
    user_feedback = [
        {        
            'name': 'Ashleigh',
            'comments': "Joe is honestly a wee ray of sunshine. Not like the vast majority of pts out there trying to sell a quick fix, she’s all about empowering the body you have and encouraging body positivity. Feel amazing after my workouts with her. Great value for money and the fact she is mobile is a huge plus. Would recommend to everyone :)"
        },
        {
            'name': 'Kelly',
            'comments': "Been training with Joe for over two months now and can’t believe I actually look forward to our session. She knows how to push you and when to step back, cannot recommend her enough "
        },
        {
            'name': 'Robyn',
            'comments': "Been working with Joe for some time now and I’ve never felt so good about myself both mentally and physically. She pushes me in the nicest way possible and celebrates all my achievements which really makes me feel that bit more accomplished. I’ve never viewed fitness with such an air of positivity until I started working with Joe, I cannot recommend her enough to everyone; novices, those looking for a challenge and everything in between! Thank you for everything!"
        }
    ]
    context = {
        'title': 'Home',
        'nbar': 'home',
        'user_feedback': user_feedback
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About',
        'nbar': 'about'
    }
    return render(request, 'about.html', context)
