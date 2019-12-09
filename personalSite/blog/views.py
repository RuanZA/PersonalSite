from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'RuanZA',
        'title':'Blog Post 1',
        'content' : 'First post',
        'date_posted' : '121212'
    },
    {
        'author': 'RuanZA',
        'title': 'Blog Post 2',
        'content': 'First post 2',
        'date_posted': '121212'
    },
    {
        'author': 'RuanZA',
        'title': 'Blog Post 3',
        'content': 'First post 3',
        'date_posted': '121212'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
