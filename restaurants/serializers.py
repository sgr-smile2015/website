from rest_framework import serializers
from .models import RestaurantsLocation


class RestaurantSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantsLocation
        fields = ('name', 'location', 'category')
