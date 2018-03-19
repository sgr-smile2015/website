from django.shortcuts import render
from random import randint
#from django.http import HttpResponse

from django.views.generic import TemplateView
from django.views import View


class AboutView(TemplateView):
    template_name = 'mysite/about.html'


class ContactView(TemplateView):
    template_name = 'mysite/contact.html'


class HomeView(TemplateView):

    template_name = 'mysite/home.html'

    def get_context_data(self, **kwargs):
        #context = super(HomeView, self).get_context_data(**kwargs)

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
