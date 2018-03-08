from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from common import base_admin
from .utils import table_filter


def index(request):
    #print(base_admin.enabled_admins)
    return render(request, 'common/index.html', {'table_list': base_admin.enabled_admins})


def display_table_objs(request, app_name, table_name):
    #print("-->{app} {table}" .format(app=app_name, table=table_name))
    admin_class = base_admin.enabled_admins[app_name][table_name]

    object_list, filter_conditons = table_filter(request, admin_class)
    paginator = Paginator(object_list, admin_class.list_per_page)

    page = request.GET.get('page')
    try:
        query_sets = paginator.page(page)
    except PageNotAnInteger:
        query_sets = paginator.page(1)
    except EmptyPage:
        query_sets = paginator.page(paginator.num_pages)

    return render(request, 'common/table_objs.html', {"admin_class": admin_class,
                                                      "query_sets": query_sets,
                                                      "filter_conditions": filter_conditons})
