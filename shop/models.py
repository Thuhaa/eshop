from django.db import models
import datetime
from django.utils.crypto import get_random_string #--Decided not to use this because of a bug that makes it return the same string as before
import time

PRODUCT_CATEGORIES = (
	('Men','Men'), ('Women', 'Women'),
	('Kids','Kids'),('Accesories','Accesories'), 
	('Footwear','Footwear')
	)

TAG_CHOICES = (
	('Hot','Hot'), ('New', 'New')
	)


# Once this model is created, run migrations to create a table for it in the database
class Product(models.Model):
	'''The Generic Produc Model'''
	unique_sku = models.CharField(max_length=50, unique=True)
	product_name = models.CharField(max_length=200)
	product_image = models.ImageField(upload_to='product_images/') # Needs to install Pillow, must be an absolute path. Not a relative path
	product_category = models.CharField(max_length=50, choices=PRODUCT_CATEGORIES)
	description = models.TextField(blank=True)
	price = models.CharField(max_length=100, blank=True)
	percentage_discount = models.CharField(max_length=4, blank=True, null=True)
	tag = models.CharField(max_length=10, choices=TAG_CHOICES, blank=True, null=True)
	date_posted = models.DateTimeField(auto_now=True)
	in_stock = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.product_name

	class Meta:
		verbose_name_plural = "Products"

# This is the model image that is going to be displayed on the banner image
class FeaturedProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	# The banner image should have a dimension of 1900x700
	banner_image = models.ImageField(upload_to='banner_images/')
	title_text = models.CharField(max_length=200)
	special_text = models.CharField(max_length=200, blank=True, null=True)
	explanation_text = models.TextField(max_length=300, blank=True, null=True)

	def __str__(self):
		return self.title_text

	class Meta:
		verbose_name_plural = "Featured Products"