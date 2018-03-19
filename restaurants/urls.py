from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="index"),
    url(r'^about$', views.AboutView.as_view(), name="about"),
    url(r'^contact$', views.ContactView.as_view(), name="contact"),
    url(r'^res$', views.restaurants, name="res"),
]
