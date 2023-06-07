from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Course


def home_view(request):
    ## add popular courses later
    courses = Course.objects.all()
    popular_courses = Course.objects.filter(is_featured=True)
    context = {'courses': courses, 'popular_courses': popular_courses}
    return render(request, 'home.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # login if anthenticate success
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = 'Incorrect Username or Password Entered'
            messages.error(request, message)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # throw error when user exists
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('home')
        except IntegrityError:
            messages.error(request, 'Username Already Exists')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'User Logged Out')
    return redirect('login')

def my_courses_view(request):
    return render(request, 'home.html')