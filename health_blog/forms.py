from django import forms
from .models import Blog, Question, Answer


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'headline', 'image', 'content', 'content_image', 'instructions')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content',)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content', 'star_question')
