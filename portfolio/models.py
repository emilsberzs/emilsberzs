from django.db import models
from django.urls import reverse


class Projects (models.Model):
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    stack = models.CharField(max_length=500)
    description = models.TextField()
    repo = models.URLField(blank=True)
    screenshot = models.ImageField(blank=True)
    slug = models.SlugField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:projects_detail', args=[self.id, self.slug])
