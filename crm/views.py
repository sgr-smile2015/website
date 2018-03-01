from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sales_index(request):
    return render(request, 'sales/customer.html')

