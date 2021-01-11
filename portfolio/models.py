from django.db import models


class Projects (models.Model):
    title = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    stack = models.CharField(max_length=500)
    description = models.TextField()
    repo = models.URLField(blank=True)

    def __str__(self):
        return self.title
