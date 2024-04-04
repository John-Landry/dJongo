from django.shortcuts import render

posts = [
    {
        'author': 'John Landry', 
        'title': 'First Blog',
        'content': 'Thoughts',
        'date_posted': 'April 1, 2022'
    },
    {
        'author': 'Joe Smith', 
        'title': 'second Blog',
        'content': 'Thots',
        'date_posted': 'April2, 2022'
    }
    
]

def home(request):
    context = {
         'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})