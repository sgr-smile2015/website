# _*_ coding: utf-8 _*_

from rest_framework import viewsets
from .models import RestaurantsLocation
from .serializers import RestaurantSerialiezer
from rest_framework.generics import ListAPIView


class RestaurantsAPI(ListAPIView):
    queryset = RestaurantsLocation.objects.all()
    serializer_class = RestaurantSerialiezer
