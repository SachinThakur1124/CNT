from django.shortcuts import render
from .models import  *

# Create your views here.

def home(request):
    allData = Courses.objects.all();
    return render(request,'home.html',{'allData':allData})