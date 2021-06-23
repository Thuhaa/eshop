from django.shortcuts import render
from django.http import HttpResponse


def shop_home(request):
	'''
	The index page of the shop. This is where all the products will be displayed. First click to the domain will redirect here
	'''
	return render(request, 'shop/shop_home.html')
