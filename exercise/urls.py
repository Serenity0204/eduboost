# exercises/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.exercise_view, name="coding_exercise"),
    path(
        "<int:exercise_id>/", views.exercise_detail_view, name="coding_exercise_detail"
    ),
]
