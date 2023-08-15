from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/search/", views.profile_search_view, name="profile_search"),
    path("courses/", views.courses_view, name="courses"),
    path("courses/<int:course_id>/", views.course_detail_view, name="course_detail"),
    path("courses/<int:course_id>/enroll", views.enroll_view, name="enroll"),
    path("courses/<int:course_id>/unenroll", views.unenroll_view, name="unenroll"),
    path("courses/search/", views.search_view, name="search"),
]
