from django.db import models

# Create your models here.

class ProductCategory(models.Model):
	name = models.CharField(max_length=64, unique=True)
	description = models.TextField(blank=True, null=True)

class Product(models.Model):
	name = models.CharField(max_length=256)
	image = models.ImageField(upload_to='products_images', blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	quantity = models.PositiveIntegerField(default=0)
	category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

