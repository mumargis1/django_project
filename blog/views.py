from django.shortcuts import render
from django.http import HttpResponse
from sympy import content

posts = [
    {
        'author':'author1', 
        'title':'Blog post 1', 
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author':'author2',
        'title':'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Augest 28, 2018'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    # return HttpResponse('<h1>Blog Home </h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1> Blog About </h1>')
    return render(request, 'blog/about.html', {'title':': About'})
