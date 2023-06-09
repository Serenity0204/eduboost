from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from .models import Course


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        # login if anthenticate success
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            message = "Incorrect Username or Password Entered"
            messages.error(request, message)
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # throw error when user exists
        try:
            user = User.objects.create_user(
                username=username, password=password, email=email
            )
            login(request, user)
            return redirect("home")
        except IntegrityError:
            messages.error(request, "Username Already Exists")
            return redirect("register")
    else:
        return render(request, "register.html")


def logout_view(request):
    logout(request)
    messages.success(request, "User Logged Out")
    return redirect("login")


def home_view(request):
    popular_courses = Course.objects.filter(is_featured=True)
    context = {"popular_courses": popular_courses}
    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")


def courses_view(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "courses.html", context)


def search_view(request):
    query = request.GET.get("query")
    if query:
        courses = Course.objects.filter(title__startswith=query)
    else:
        courses = []
    context = {"courses": courses, "query": query}
    return render(request, "search.html", context)


@login_required(login_url="login")
def profile_view(request):
    user = request.user
    courses = user.courses.all()
    context = {'courses': courses}
    return render(request, 'profile.html', context)


@login_required(login_url="login")
def enroll_view(request, course_id):
    course = Course.objects.get(id=course_id)
    request.user.courses.add(course)
    return redirect("profile")


@login_required(login_url="login")
def unenroll_view(request, course_id):
    course = Course.objects.get(id=course_id)
    request.user.courses.remove(course)
    return redirect("profile")


@login_required(login_url="login")
def course_detail_view(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = None
    is_enrolled = False
    enrollment_list = course.students.all()
    if request.user in enrollment_list:
        is_enrolled = True
        lessons = course.lessons.all()
    context = {"course": course, "lessons": lessons, "is_enrolled": is_enrolled}
    return render(request, "course_detail.html", context)
