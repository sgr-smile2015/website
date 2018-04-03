from django.conf.urls import url
from . import views
from . import api

from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^about$', views.AboutView.as_view(), name="about"),
    url(r'^login$', views.RestaurantsListViews.as_view(), name="login"),
    url(r'^contact$', views.ContactView.as_view(), name="contact"),
    url(r'^res/$', views.RestaurantsListViews.as_view(), name="list"),
    url(r'^res/create/$', views.RestaurantsFormCreate.as_view(), name="create"),
    #url(r'^res/create/$', views.restaurants_create, name="create"),
    url(r'^res/(?P<rest_id>\d+)/$', views.RestaurantsDetailViews.as_view(), name="ResDetailViews"),
    url(r'^res/(?P<slug>[\w-]+)/$', views.RestaurantsDetailViews.as_view(), name="detail"),
    url(r'^v1/users/$', api.RestaurantsAPI.as_view(), name="ResAPI"),
    #url(r'^res/(?P<slug>\w+)/$', views.RestaurantsDetailViews.as_view(), name="ResDetail"),
]
