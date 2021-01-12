from django.contrib import admin
from .models import Projects


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'start_date', 'stack', 'description', 'repo', 'slug')
    list_display = ('title', 'start_date')
    prepopulated_fields = {'slug': ('title',)}
