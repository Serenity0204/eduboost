from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects_view, name="projects"),
    path("<int:project_id>/", views.project_detail_view, name="project_detail"),
    path("search/", views.project_search_view, name="project_search"),
]
