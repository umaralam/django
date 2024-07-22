"""
    Import
"""
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    """
        Tag
    """
    tag = models.CharField(max_length=255)

class TaggedItem(models.Model):
    """
        Tagged Item
    """
    #what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #in table
    #Type (Product, Vedio, Article)
    #ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
