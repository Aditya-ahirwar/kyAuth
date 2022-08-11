import email
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'userAuth/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered.")
            return redirect('signup')
        
        newUser = User.objects.create_user(username, email, password)
        newUser.name = name
        newUser.save()
        messages.success(request, f"Congratulation {name} you are registered.")
        return redirect('signup')

    return render(request, 'userAuth/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(username = username, password = password)
        if User is not None:
            login(request, User)
            email = User.email
            return render(request, 'userAuth/index.html', {'name': username, 'email' : email})
        else:
            messages.error(request, "Wrong username or password")
    return render(request, 'userAuth/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('signup')