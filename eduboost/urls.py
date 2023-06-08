from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("courses/<int:course_id>/", views.course_detail_view, name="course_detail"),
    path("courses/", views.courses_view, name="courses"),
]
