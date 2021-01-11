from django.urls import path
from .views import ProjectListView

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='project_list'),
]