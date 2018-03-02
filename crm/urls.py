from django.conf.urls import url
from . import views

#app_name = 'crm'

urlpatterns = [
    url(r'^$', views.index, name="sales_index"),
    url(r'^customer/$', views.customer_list, name="customer_list"),
]
