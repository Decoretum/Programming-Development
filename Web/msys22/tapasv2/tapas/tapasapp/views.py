import re
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish,Account
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth

# I hereby attest to the truth of the following facts:
# I have not discussed the <programming language used> language code in my program
# with anyone other than my instructor or the teaching assistants assigned to this course.
# I have not used <programming language used> language code obtained from another
# student, or any other unauthorized source, either modified or unmodified.
# If any <programming language used> language code or documentation used in my
# program was obtained from another source, such as a text book or course notes, that has
# been clearly noted with a proper citation in the comments of my program. 

def login_person(request):
    if(request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')  
        userinitial = authenticate(request, username=username, password=password)
        if userinitial is not None:
            login(request, userinitial)
            userobj = get_object_or_404(Account, username=username, password=password )
            request.session['user'] = userobj.username
            request.session['userid'] = userobj.pk
            request.session['password'] = userobj.password
            return redirect('better_menu')
        else:
            messages.info(request,'Invalid credentials for login')
            return redirect('login')
    else:
        return render(request,'tapasapp/login.html')

def error(request):
    return render(request, 'tapasapp/error.html')

def signup(request):
    if (request.method=='POST'):
        user = request.POST.get('usern')
        passw = request.POST.get('passn')
        if User.objects.filter(username=user).exists():
            messages.info(request,'Username is already taken')
            return redirect('signup')
        else:
            Account.objects.create(username=user, password=passw) 
            #model creation
    
            userobject = User.objects.create_user(username=user, password=passw)
            userobject.save()
            #registration of user object to auth model

            return redirect('login')
            
    else:
        return render(request, 'tapasapp/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def basic_list(request):
    accounts = Account.objects.all()
    return render(request, 'tapasapp/basic_list.html', {'a':accounts, 'user': request.session['user'], 'id': request.session['userid']})


def manage_account(request,pk):
    d = get_object_or_404(Account, pk=pk)
    return render(request, 'tapasapp/manage_account.html', {'u': d,})

def delete_user(request,pk):
    usermodel = Account.objects.get(pk=pk)
    User.objects.filter(username=usermodel.username).delete()
    usermodel.delete()
    auth.logout(request)
    return redirect('login')

def change(request,pk):
    if(request.method=='POST'):
        old = request.POST.get('current')
        cur = request.POST.get('new') 
        curagain = request.POST.get('newagain') 
        me = Account.objects.get(pk=pk)
        mypass = User.objects.get(username=me.username)
        if old != request.session['password'] and cur != curagain:
            messages.info(request,'Incorrect current password and new passwords do not match')
            return redirect('change', pk=pk)
        elif old != request.session['password'] and cur == curagain:
            messages.info(request,'Incorrect current password')
            print(mypass)
            return redirect('change', pk=pk)
        elif old == request.session['password'] and cur != curagain:
            messages.info(request, 'New and Retyped passwords do not match')
            return redirect('change', pk=pk)  
        else:
            mypass.set_password(cur)
            mypass.save()
            Account.objects.filter(pk=pk).update(password=cur)
            request.session['password'] = cur
            return redirect('manage_account', pk=pk )

    else:
        u = get_object_or_404(Account,pk=pk)
        return render(request, 'tapasapp/change.html', {'u':u, 'pass':request.session['password']})

def view_menu(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/list.html', {'dishes':dish_objects})


def better_menu(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/better_list.html', {'dishes':dish_objects, 'person': request.session['user']})

def add_menu(request):
    if(request.method=="POST"):
        dishname = request.POST.get('dname')
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.create(name=dishname, cook_time=cooktime, prep_time=preptime)
        return redirect('better_menu')
    else:
        return render(request, 'tapasapp/add_menu.html',{'person': request.session['user']})
    

def view_detail(request, pk):
    d = get_object_or_404(Dish, pk=pk)
    return render(request, 'tapasapp/view_detail.html', {'d': d, 'person': request.session['user']})

def delete_dish(request, pk):
    Dish.objects.filter(pk=pk).delete()
    return redirect('better_menu')

def update_dish(request, pk):
    if(request.method=="POST"):
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.filter(pk=pk).update(cook_time=cooktime, prep_time=preptime)
        return redirect('view_detail', pk=pk)
    else:
        d = get_object_or_404(Dish, pk=pk)
        return render(request, 'tapasapp/update_menu.html', {'d':d, 'person': request.session['user']})