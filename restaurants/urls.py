from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="index"),
    url(r'^about$', views.AboutView.as_view(), name="about"),
    url(r'^contact$', views.ContactView.as_view(), name="contact"),
    url(r'^res/$', views.RestaurantsListViews.as_view(), name="res"),
    url(r'^res/create/$', views.RestaurantsFormCreate.as_view(), name="create"),
    url(r'^res/(?P<rest_id>\d+)/$', views.RestaurantsDetailViews.as_view(), name="ResDetailViews"),
    url(r'^res/(?P<slug>[\w-]+)/$', views.RestaurantsDetailViews.as_view(), name="ResListViews"),
    #url(r'^res/(?P<slug>\w+)/$', views.RestaurantsDetailViews.as_view(), name="ResDetail"),
]
