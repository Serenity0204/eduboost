from django.contrib import admin
from .models import Course, Lesson, Video
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    exclude = ('students',)
admin.site.register(Course, CourseAdmin)


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    inlines = [VideoInline]


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Video)