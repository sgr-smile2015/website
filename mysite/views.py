from django.shortcuts import render
from random import randint
#from django.http import HttpResponse


def index(request):
    html_var = 'f string'
    num = randint(0,100000)
    some_list = [num, randint(0,100000), randint(0,100000)]
    context = {
        'boll_var': True,
        'num': num,
        'some_lists': some_list
    }

    return render(request, 'page.html', context)

