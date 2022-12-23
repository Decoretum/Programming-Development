from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Userperson, Product
from django.contrib.auth import authenticate,login
#from django.contrib.auth.models import auth, User
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    #Product.objects.create(Name = "NanoLaser",Brand = "NanoTechPH", Color = "Blue",Cost = "P5000")
    return render(request, 'Inventory/home.html')

def Products(request):
    P = Product.objects.all()
    return render(request, 'Inventory/products.html',{'P':P})


    

#def Order(request):



    