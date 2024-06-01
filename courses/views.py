from django.shortcuts import render
from home.models import *

# Create your views here.

def courses(request):
    allData = Courses.objects.all();
    return render(request,'courses.html', { "allData" : allData})