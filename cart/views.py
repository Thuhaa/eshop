from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from shop.models import Product



def cart_detail(request):
	cart = Cart(request)
	items_in_cart = []
	return render(request, 'cart/cart_detail.html', {'cart':cart})



def add_to_cart(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	cart = Cart(request)
	cart.add(product=product, quantity=1, override_quantity=False)
	print(type(cart))
	return redirect('cart-detail')


# Create your views here.
