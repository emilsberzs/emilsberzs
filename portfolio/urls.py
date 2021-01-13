from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('list/', views.project_list, name='project_list'),
    path('<int:id>/<slug:slug>/', views.project_detail, name='projects_detail'),

]
