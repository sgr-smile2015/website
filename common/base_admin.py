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
    """
    model_class: Customer class
    admin_class: CustomerAdmin class
    :return: 构造一个新字典 {"crm":{'customer':customer_admin}}
    """
    if model_class._meta.app_label not in enabled_admins:
        #enabled_admins['crm'] = {}
        enabled_admins[model_class._meta.app_label] = {}

    #绑定model对象和admin类
    admin_class.model = model_class
    #enabled_admins['crm']['customer'] = CustomerAdmin
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class


register(models.Customer, CustomerAdmin)
register(models.CustomerFollowUp, CustomerFollowUpAdmin)
