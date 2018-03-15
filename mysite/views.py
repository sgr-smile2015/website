from django.shortcuts import render
from random import randint
#from django.http import HttpResponse

from django.views.generic import TemplateView


def about(request):
    return render(request, 'mysite/about.html')


def contact(request):
    return render(request, 'mysite/contact.html')


class HomeView(TemplateView):

    template_name = 'mysite/home.html'
    #return super(HomeView, self).get_context_data(**kwargs)

    def get_context_data(self, **kwargs):
        html_var = 'git string'
        num = randint(0, 100000)
        some_list = [randint(0, 100000),
                     randint(0, 100000),
                     randint(0, 100000)]
        context = {
            'boll_var': True,
            'html_var': html_var,
            'num': num,
            'some_lists': some_list
        }
        return context
