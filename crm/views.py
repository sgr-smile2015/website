from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def customer_list(request):
    return render(request, 'sales/customer.html')

