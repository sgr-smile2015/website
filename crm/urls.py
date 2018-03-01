from django.conf.urls import url
from . import views

app_name = 'crm'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sales/$', views.customer_list, name='sales_index'),
]
