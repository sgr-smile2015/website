# coding: utf-8
# author: sgr


def table_filter(request, admin_class):
    filter_conditions = {}

    for k, v in request.GET.items():
        print(k, v)
        filter_conditions[k] = v

    return admin_class.model.objects.filter(**filter_conditions), filter_conditions
