from django.shortcuts import render
from random import randint
#from django.http import HttpResponse
from django.db.models.query_utils import Q

from django.views.generic import TemplateView, ListView
from django.views import View

from .models import RestaurantsLocation


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


def restaurants(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantsLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


class RestaurantsListViews(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        print(slug)
        if slug:
            queryset = RestaurantsLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug))
        else:
            queryset = RestaurantsLocation.objects.all()
        return queryset

