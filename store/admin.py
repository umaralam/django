"""
    Import section
"""
from typing import Any
from django.contrib import admin, messages
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from . import models

class InventoryFilter(admin.SimpleListFilter):
    """
        custome list page filter
    """
    title = 'inventory'
    parameter_name = 'inventory'
    
    def lookups(self, request, model_admin):
        lt_10 = '<10'
        return [
            (lt_10, 'Low')
        ]
    
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
    
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    """
        collection list page
    """
    search_fields = ['title']
    list_display = ['title', 'products_count']
    list_per_page = 10

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        """
            display products count for each collection
        """
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                   'collection__id' : str(collection.id)
               }))
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count = Count('products')
        )

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """
        product list page
    """
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status',
                    'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['title__istartswith']
    
    def collection_title(self, product):
        """
            display collection title for each product
        """
        return product.collection.title
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        """
            display inventory status for each product
        """
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        """
            clearing inventory
        """
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfuly updated.',
            messages.ERROR
        )
    
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
        customer list page
    """
    list_display = ['first_name', 'last_name', 'memberships', 'orders_count']
    list_editable = ['memberships']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith']
    
    @admin.display(ordering='orders_count')
    def orders_count(self, customer):
        """
            display order for each customer
        """
        url = (reverse('admin:store_order_changelist')
                      + '?'
                      + urlencode({
                         'customer__id' : str(customer.id) 
                      }))
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)
        
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            orders_count = Count('order')
        )
        

class OrderItemedInline(admin.StackedInline):
    """
        editing children using inline
    """
    autocomplete_fields = ['product']
    extra = 0
    min_num = 1
    max_num = 10
    model = models.OrderItem
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    """
        order list page
    """
    autocomplete_fields = ['customer']
    inlines = [OrderItemedInline]
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 10

