from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib import messages
from .forms import SignUpForm


def register_user(request):
    '''
	Register Users Function. To be expanded later with the addition of AJAX and others
	'''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = form.save()
            login(request, user)
            return redirect('shop_home')
        if form.errors == "My customers with this email address already exists":
            form.errors="Users with this email address already exists"
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'authentication/register.html', context)


# TODO: BUG!!! Users registered using the clients' register form cannot log in again.
# TODO: SUGGESTED SOLUTION TO WORK WITH THIS!!: Create a UserCreationForm and a UserChageForm
def login_user(request):
    '''
	Login users
	'''
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, password: {password}")
        user = authenticate(email=email, password=password)
        if user is not None:
            print(user is not None)
            login(request, user)
            return redirect('shop_home')
        else:
            print("User not found")
            messages.success(request, ("User does Not Exist"))
            return redirect('login')
    return render(request, 'authentication/login.html')


def index_page(request):
    return render(request, 'authentication/index.html')
# Create your views here.
