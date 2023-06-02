from django.contrib import admin
from .models import Course, Lesson, Video
# Register your models here.

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Lesson)