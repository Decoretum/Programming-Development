from django.shortcuts import render
from .models import Hero

# Create your views here.

def seemywrath(request):
    gael_objects = Hero.objects.all()
    return render(request, 'myapp/hello_world.html', {'Heroes':gael_objects})

def seeitall(request):
    gael_objects = Hero.objects.all()
    return render(request, 'myapp/hello_world.html', {'Heroes':gael_objects})