from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been Logged In!')
            return redirect('website:home')
        
        else:
            messages.success(request, "There was an error logging in, please try Again...")
            return redirect('website:home')


    context = {}
    return render(request, 'website/home.html', context)



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('website:home')

def register_user(request):
    context = {}
    return render(request, 'website/register.html', context)