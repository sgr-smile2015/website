from django.shortcuts import render
from common import base_admin


def index(request):
#    print(base_admin.enabled_admins)
    return render(request, 'common/index.html', {'table_list': base_admin.enabled_admins})


def display_table_objs(request, app_name, table_name):
    print("-->{app} {table}" .format(app=app_name, table=table_name))
    content = str(table_name)
    return render(request, 'common/table_objs.html', {"content": content})
