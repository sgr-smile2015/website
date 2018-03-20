from django.db import models


class RestaurantsLocation(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32, null=True, blank=True)
    category = models.CharField(max_length=128, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
