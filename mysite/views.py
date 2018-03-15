from django.shortcuts import render
from random import randint
#from django.http import HttpResponse


def index(request):
    html_var = 'f string'
    num = randint(0, 100000)
    some_list = [num, randint(0, 100000), randint(0, 100000)]
    context = {
        'boll_var': True,
        'html_var': html_var,
        'num': num,
        'some_lists': some_list
    }

    return render(request, 'mysite/home.html', context)


def about(request):
    return render(request, 'mysite/about.html')


def contact(request):
    return render(request, 'mysite/contact.html')
