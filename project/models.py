from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)  # New field for GitHub URL

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    code_snippet = models.TextField(blank=True, null=True)
    section = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="sections"
    )
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
