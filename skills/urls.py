from django.urls import path
from .views import skills_list_view

app_name = 'skills'

urlpatterns = [
    path('all/', skills_list_view, name='skill_list'),
]
