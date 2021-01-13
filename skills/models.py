from django.db import models


class Skills (models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(blank=True)
    description = models.TextField()
