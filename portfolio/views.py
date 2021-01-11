from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
from django.views.generic import ListView


def home_page(request):
    return render(request, 'home.html')


class ProjectListView(ListView):
    model = Projects
    projects = Projects.objects.all()
    template_name = 'projects_list.html'
