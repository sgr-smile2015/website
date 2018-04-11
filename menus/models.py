from django.db import models
from django.conf import settings
from restaurants.models import RestaurantsLocation


class ResItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(RestaurantsLocation)

    name = models.CharField(max_length=128)
    content = models.TextField(help_text='separate each item by comma')
    excludes = models.TextField(blank=True, null=True, help_text='separate Each Item')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-uptime', '-timestamp']

    def get_contents(self):
        return self.content.split(',')

    def get_excludes(self):
        return self.excludes.split(',')
