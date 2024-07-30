import email
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product
from store.models import OrderItem
# Create your views here. Request handler
# def say_hello(request):
#     return HttpResponse("Hello World")


def say_hello(request):
    # queryset = Customer.objects.filter(email__icontains=".com") # pylint: disable=no-member
    # queryset = Collection.objects.filter(featured_product_id__isnull=False) # pylint: disable=no-member
    # queryset = Product.objects.filter(Q(inventory__lt=10) &
    #                                   ~Q(unit_price__lt=20)) # pylint: disable=no-member
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # queryset = Product.objects.filter(collection_id=1).order_by('unit_price')
    # product = Product.objects.order_by('unit_price')[0]
    # queryset = Product.objects.all()[0:5]
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = OrderItem.objects.values('product_id').distinct()
    queryset = Product.objects.values('description')
    return render(request, 'hello.html', {'name': 'Md Umar Alam', 'products': list(queryset)})
