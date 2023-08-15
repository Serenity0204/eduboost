from django.db import models
from django.contrib.auth.models import User


def get_default_image():
    # Define the path to your default image
    return "path/to/default/image.jpg"


class Course(models.Model):
    title = models.CharField(max_length=30, default="course")
    description = models.TextField(max_length=1000)
    students = models.ManyToManyField(User, related_name="courses")
    preview_img = models.ImageField(upload_to="images/", default=get_default_image)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=30, default="lesson")

    def __str__(self):
        return self.title


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="videos")
    youtube_link = models.URLField()
    title = models.CharField(max_length=30, default="video")

    def __str__(self):
        return self.title
