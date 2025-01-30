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

class Product(models.Model):
    
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from='name')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/%d,%m,%Y')
    created_at = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} with {self.price}'