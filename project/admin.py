from django.contrib import admin
from .models import Project, Section


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


admin.site.register(Project, ProjectAdmin)
