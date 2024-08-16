"""
Import section
"""
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem

class TagInLine(GenericTabularInline):
    """
        product tagging
    """
    autocomplete_fields = ['tag']
    extra = 0
    model = TaggedItem

class CustomProductAdmin(ProductAdmin):
    """
        custom product admin
    """
    inlines = [TagInLine]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
