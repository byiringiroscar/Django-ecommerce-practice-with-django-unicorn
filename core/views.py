from django.shortcuts import render
from core.models import *


# Create your views here.

def home(request):
    products = Product.objects.all()
    customer, created = Customer.objects.get_or_create(user=request.user)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {
        'products': products,
        'order': order
    }
    return render(request, 'home.html', context)


def shop(request):
    products = Product.objects.all()
    customer, created = Customer.objects.get_or_create(user=request.user)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {
        'products': products,
        'order': order
    }
    return render(request, 'shop.html', context)
