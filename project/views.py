from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from django.core.paginator import Paginator
from django.http import FileResponse


def projects_view(request):
    request.session.set_expiry(900)

    projects_list = Project.objects.all()

    paginator = Paginator(projects_list, 5)  # Show 5 projects per page.

    page_number = request.GET.get("page")

    projects = paginator.get_page(page_number)

    context = {"projects": projects}

    return render(request, "projects.html", context)


@login_required(login_url="login")
def project_detail_view(request, project_id):
    request.session.set_expiry(900)
    project = get_object_or_404(Project, pk=project_id)
    context = {"project": project}
    return render(request, "project_detail.html", context)
