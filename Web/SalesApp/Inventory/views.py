from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Position,Candidate,Userperson, Vote
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import auth, User
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def signup(request):
    