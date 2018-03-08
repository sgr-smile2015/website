# coding: utf-8
# author: sgr


def table_filter(request, admin_class):
    filter_conditions = {}

    for k, v in request.GET.items():
        if k == 'page':
            continue
        if v:
            filter_conditions[k] = v
            print(filter_conditions)

    return admin_class.model.objects.filter(**filter_conditions), filter_conditions
