from django.contrib import admin
from .models import Product, FeaturedProduct

class ProductAdmin(admin.ModelAdmin):
	list_display = [
	'unique_sku', 'product_name', 
	'product_category', 'price' ,
	'percentage_discount', 'tag', 
	'date_posted', 'in_stock'
	]
class FeaturedProductAdmin(admin.ModelAdmin):
	list_display = [
	 'product', 'title_text', 'special_text'
	]

admin.site.register(Product, ProductAdmin)
admin.site.register(FeaturedProduct, FeaturedProductAdmin)
# Remember to makemigrations for the models you create
