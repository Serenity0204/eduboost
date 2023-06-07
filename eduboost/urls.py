from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("my_courses/", views.my_courses_view, name="my_courses"),
    path("<int:course_id>/", views.course_detail_view, name="course_detail"),
]
