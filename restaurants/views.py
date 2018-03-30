from django.shortcuts import render, get_object_or_404
from random import randint
from django.http import HttpResponseRedirect
from django.db.models import Q

from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views import View

from .models import RestaurantsLocation
from .form import RestaurantsCreateForm, RestaurantsLocationCreateForm


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


def restaurants_create(request):
    template_name = 'restaurants/form.html'
    form = RestaurantsCreateForm(request.POST or None)
    error = form.errors

    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/res/')
        #name = form.cleaned_data.get('name')
        #location = form.cleaned_data.get('location')
        #category = form.cleaned_data.get('category')
        #obj = RestaurantsLocation.objects.create(
        #    name=name,
        #    location=location,
        #    category=category
        #)
        #return HttpResponseRedirect('/res/')
    if form.errors:
        print(form.errors)
    context = {
        'form': form,
        'error': error
    }
    return render(request, template_name, context)


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
        if slug:
            q = RestaurantsLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug))
        else:
            q = RestaurantsLocation.objects.all()
        return q


class RestaurantsDetailViews(DetailView):
    template_name = 'restaurants/restaurants_detail.html'
    queryset = RestaurantsLocation.objects.all()

    #def get_context_data(self, **kwargs):
    #    print(kwargs)
    #    #context = super(RestaurantsDetailViews, self).get_context_data(**kwargs)
    #    return 1

    #def get_object(self, queryset=None):
    #    rest_id = self.kwargs.get('rest_id')
    #    #pk = rest_id
    #    obj = get_object_or_404(RestaurantsLocation, id=rest_id)
    #    return obj


class RestaurantsFormCreate(CreateView):
    template_name = 'restaurants/form.html'
    form_class = RestaurantsLocationCreateForm
    success_url = '/res/'

