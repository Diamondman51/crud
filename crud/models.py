from django.contrib.auth.models import AbstractUser

from django.db import models

from django.db import models
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='product/images/')
    file = models.FileField(null=True, blank=True, upload_to='product/files/')
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
    def __str__(self):
        return self.name if self.name else 'No Name'


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='product/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='product/files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
