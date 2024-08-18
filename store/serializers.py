"""
    import section
"""
from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    """
        collection model serializer
    """
    class Meta:
        """
            meta data
        """
        model = Collection
        fields = ['id', 'title', 'products_count']
        
    products_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    """
        product model serializer
    """
    class Meta:
        """
            Meta data
        """
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'unit_price', 'inventory',\
            'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        """
            calculate tax
        """
        return product.unit_price * Decimal(1.1)
    