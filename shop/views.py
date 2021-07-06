from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, FeaturedProduct
from cart.cart import Cart

def shop_home(request):
	'''
	The index page of the shop. This is where all the products will be displayed. First click to the domain will redirect here
	'''
	current_user = request.user
	cart = Cart(request)
	products = Product.objects.all()
	featured_products = FeaturedProduct.objects.all()
	ladies_products = Product.objects.filter(product_category="Women")
	mens_products = Product.objects.filter(product_category="Men")
	kids_products = Product.objects.filter(product_category="Kids")
	accesories = Product.objects.filter(product_category="Accesories")
	hot_items = Product.objects.filter(tag="Hot")


	context = {
	'products':products,
	'featured_products':featured_products,
	'ladies_products':ladies_products,
	'mens_products':mens_products,
	'kids_products':kids_products,
	'accesories':accesories,
	'hot_items':hot_items
	}
	return render(request, 'shop/shop_home.html', context)

def redirect_to_shop(request):
	return redirect('shop_home')


