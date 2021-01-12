from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Projects
from django.views.generic import ListView, DetailView


def home_page(request):
    return render(request, 'home.html')


def project_list(request):
    projects = Projects.objects.all()
    return render(request, 'projects_list.html', {'projects': projects})


def project_detail(request, id, slug):
    project = get_object_or_404(Projects, id=id, slug=slug)
    return render(request, 'projects_detail.html', {'project': project})
