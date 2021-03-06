from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.core.urlresolvers import reverse

from .util import unique_slug_generator


User = settings.AUTH_USER_MODEL


class RestaurantsLocation(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32, null=True, blank=True)
    category = models.CharField(max_length=128, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('res:detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    # print('save...')
    # print(instance.timestamp)
    if not instance.slug:
        #instance.name = 'Anoter new title'
        instance.slug = unique_slug_generator(instance)


def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
    print('Saved')
    print(instance.timestamp)


pre_save.connect(rl_pre_save_receiver, sender=RestaurantsLocation)
#post_save.connect(rl_post_save_receiver, sender=RestaurantsLocation)
