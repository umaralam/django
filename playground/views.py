from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.db.models import Q, F, DecimalField, IntegerField, Value, Func, ExpressionWrapper
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Concat
from django.db.models.aggregates import Avg, Min, Max, Count, Sum
from store.models import Customer, Order, Product, OrderItem, Collection, Cart, CartItem
from tags.models import TaggedItem
# Create your views here. Request handler
# def say_hello(request):
#     return HttpResponse("Hello World")

# @transaction.atomic()
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
    # queryset = Product.objects.values('description')
    # queryset = Product.objects.select_related('collection').all()
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # queryset = Order.objects.select_related('customer').\
    #                         prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # return render(request, 'hello.html', {'name': 'Md Umar Alam', 'orders': list(queryset)})
    # result = Order.objects.aggregate(count = Count('id'))
    # result = OrderItem.objects.filter(product__id=1).aggregate(units_sold=Sum('quantity'))
    # result = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))
    # result = Product.objects.filter(collection__id=3)\
    #                         .aggregate(
    #                             min_price = Min('unit_price'),
    #                             avg_price = Avg('unit_price'),
    #                             max_price = Max('unit_price')
    #                         )
    # result = Order.objects.filter(customer__id=1).aggregate(count= Count('id'))
    # queryset = Customer.objects.annotate(new_id=F('id') + 1)
    # queryset = Customer.objects.annotate(
    #     full_name = Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    # queryset = Customer.objects.annotate(
    #     full_name = Concat('first_name', Value(' '), 'last_name')
    # )
    # queryset = Customer.objects.annotate(
    #     orders_count=Count('order')
    # )
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price = discounted_price
    # )
    # queryset = Customer.objects.annotate(
    #     last_order_id = Max('order__id')
    # )
    # queryset = Collection.objects.annotate(
    #     products_count = Count('product')
    # )
    
    # queryset = Customer.objects.annotate(
    #     orders_count = Count('order')).filter(orders_count__gt=5)
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product_id = None
    # collection.save()
    # Collection.objects.filter(pk=11).update(featured_product_id=1)
    # collection = Collection.objects.create(title='Vedio Games', featured_product_id = 1)
    # with transaction.atomic():
    #     cart = Cart()
    #     cart.save()
        
    #     item1 = CartItem()
    #     item1.cart = cart
    #     item1.product_id = 1
    #     item1.quantity = 1
    #     item1.save()
    queryset = TaggedItem.objects.get_tags_for(Product, 1)
    return render(request, 'hello.html', {'name': 'Md Umar Alam', 'tags': list(queryset)})
