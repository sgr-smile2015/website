from django.shortcuts import render
from common import base_admin


def index(request):
#    print(base_admin.enabled_admins)
    return render(request, 'common/index.html', {'table_list': base_admin.enabled_admins})
