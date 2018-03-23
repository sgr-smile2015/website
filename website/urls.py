from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from restaurants import api

#router = routers.DefaultRouter()
#router.register(r'users', api.RestaurantsAPI)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('restaurants.urls')),
    url(r'^crm/', include('crm.urls')),
    url(r'^stu/', include('student.urls')),
    url(r'^comm/', include('common.urls')),
]
