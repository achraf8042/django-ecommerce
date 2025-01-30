from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(unique=True, populate_from='name')

    def __str__(self):
        return f'Category: {self.name}'
    
    class Meta:
        verbose_name_plural = 'Categories'

    