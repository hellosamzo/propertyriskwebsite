from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question


def index(request):
    return render(request, 'proprisk/index.html')

def about(request):
    return render(request, 'proprisk/about.html')    
