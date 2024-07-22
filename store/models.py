"""
    imports
"""
from django.db import models

class Promotion(models.Model):
    """
        Promotion
    """
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    start_date = models.DateTimeField(auto_created=True)
    end_date = models.DateTimeField(auto_created=True)

class Collection(models.Model):
    """
        Collection
    """
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
                                            'Product',
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='+'
                                        )

class Product(models.Model):
    """
        Product data
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    """
        Customer data
    """
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    memberships = models.CharField(
                                    max_length=1,
                                    choices=MEMBERSHIP_CHOICES,
                                    default=MEMBERSHIP_BRONZE
                                )
    

class Order(models.Model):
    """
        Order data
    """
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_created=True)
    payment_status = models.CharField(
                                        max_length=1,
                                        choices=PAYMENT_STATUS_CHOICES,
                                        default=PAYMENT_STATUS_PENDING
                                    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    """
        Order items
    """
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    """
        Cart
    """
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    """
        Cart Item
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Address(models.Model):
    """
        Customer Address
    """
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip = models.CharField(max_length=255, default=0)
