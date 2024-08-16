"""
    Import
"""
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class TaggedItemManager(models.Manager):
    """
        custome manager for taggedItem
    """
    def get_tags_for(self, obj_type, obj_id):
        """
            get tags for product
        """
        content_type = ContentType.objects.get_for_model(obj_type)
        return TaggedItem.objects \
                .select_related('tag') \
                .filter(
                        content_type = content_type,
                        object_id = obj_id
                    )
        
class Tag(models.Model):
    """
        Tag
    """
    tag = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.tag

class TaggedItem(models.Model):
    """
        Tagged Item
    """
    objects = TaggedItemManager()
    #what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #in table
    #Type (Product, Vedio, Article)
    #ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
