# coding: utf-8
# author: sgr
from crm import models

enabled_admins = {}


class BaseAdmin(object):
    list_display = []
    list_filter = []


class CustomerAdmin(BaseAdmin):
    list_display = ['qq', 'name']


class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ['customer', 'consultant', 'date']


def register(model_class, admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {}

    model_class.model = admin_class
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = model_class


register(models.Customer, CustomerAdmin)
register(models.CustomerFollowUp, CustomerFollowUpAdmin)
