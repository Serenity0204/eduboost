from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from .models import Course
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator


def login_view(request):
    if request.user.is_authenticated:
        request.session.set_expiry(
            900
        )  # Reset session expiry to 15 minutes (900 seconds)
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        # login if authenticate success
        if user is not None:
            login(request, user)
            request.session.set_expiry(
                900
            )  # Set session expiry to 15 minutes (900 seconds)
            return redirect("home")
        else:
            message = "Incorrect Username or Password Entered"
            messages.error(request, message)
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def register_view(request):
    if request.user.is_authenticated:
        request.session.set_expiry(
            900
        )  # Reset session expiry to 15 minutes (900 seconds)
        return redirect("home")
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
            request.session.set_expiry(
                900
            )  # Set session expiry to 15 minutes (900 seconds)
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
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    popular_courses = Course.objects.filter(is_featured=True)
    context = {"popular_courses": popular_courses}
    return render(request, "home.html", context)


def about_view(request):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    return render(request, "about.html")


def courses_view(request):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    courses_list = Course.objects.all()

    paginator = Paginator(courses_list, 6)  # Show 6 courses per page.
    page_number = request.GET.get("page")
    courses = paginator.get_page(page_number)

    context = {"courses": courses}
    return render(request, "courses.html", context)


def search_view(request):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    query = request.GET.get("query")
    if not query:
        return redirect("courses")

    courses_list = Course.objects.filter(title__startswith=query)
    paginator = Paginator(courses_list, 5)  # Show 5 courses per page.
    page_number = request.GET.get("page")
    courses = paginator.get_page(page_number)

    context = {"courses": courses}
    return render(request, "courses.html", context)


@login_required(login_url="login")
def profile_view(request):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    user = request.user
    courses_list = user.courses.all()

    paginator = Paginator(courses_list, 6)  # Show 6 courses per page.
    page_number = request.GET.get("page")
    courses = paginator.get_page(page_number)

    context = {"courses": courses}
    return render(request, "profile.html", context)


@login_required(login_url="login")
def profile_search_view(request):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    user = request.user

    query = request.GET.get("query")
    if not query:
        return redirect("profile")

    courses_list = user.courses.filter(title__startswith=query)

    paginator = Paginator(courses_list, 6)  # Show 6 courses per page.
    page_number = request.GET.get("page")
    courses = paginator.get_page(page_number)

    context = {"courses": courses}
    return render(request, "profile.html", context)


@login_required(login_url="login")
def enroll_view(request, course_id):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    course = Course.objects.get(id=course_id)
    request.user.courses.add(course)
    return redirect("profile")


@login_required(login_url="login")
def unenroll_view(request, course_id):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    course = Course.objects.get(id=course_id)
    request.user.courses.remove(course)
    return redirect("profile")


@login_required(login_url="login")
def course_detail_view(request, course_id):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    course = Course.objects.get(pk=course_id)
    lessons = None
    is_enrolled = False
    enrollment_list = course.students.all()
    if request.user in enrollment_list:
        is_enrolled = True
        lessons = course.lessons.all()
    context = {"course": course, "lessons": lessons, "is_enrolled": is_enrolled}
    return render(request, "course_detail.html", context)
