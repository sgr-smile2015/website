# _*_ coding: utf-8 _*_

from .models import RestaurantsLocation
from .serializers import RestaurantSerialiezer
from rest_framework.generics import ListAPIView


class RestaurantsAPI(ListAPIView):
    queryset = RestaurantsLocation.objects.all()
    serializer_class = RestaurantSerialiezer
