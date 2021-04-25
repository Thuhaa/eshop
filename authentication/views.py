from django.shortcuts import render
from django.http import HttpResponse

def sign_up(request):
	return HttpResponse("Sign Up")

def login_view(request):
	return HttpResponse("Login")
# Create your views here.
