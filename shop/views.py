from django.shortcuts import render
from django.http import HttpResponse
def shop_home(request):
	return HttpResponse("This is the Shop HomePage Where you will see all the products here!")
# Create your views here.
