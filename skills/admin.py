from django.contrib import admin
from .models import Skills


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    fields = ('title', 'logo', 'description')
    list_display = ('title',)
