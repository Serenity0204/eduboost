from django.db import models
from django.contrib.auth.models import User


def get_default_image():
    # Define the path to your default image
    return "path/to/default/image.jpg"


class Exercise(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    prewritten_code = models.TextField()
    img = models.ImageField(upload_to="images/", default=get_default_image)
    answer = models.TextField()

    def __str__(self):
        return self.title
