from django.shortcuts import render
from .models import Skills


def skills_list_view(request):
    skills = Skills.objects.all()
    return render(request, 'skills_list.html', {'skills': skills})
