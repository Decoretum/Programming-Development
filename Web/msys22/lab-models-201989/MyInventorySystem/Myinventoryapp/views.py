from multiprocessing.dummy import current_process
import re
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Supplier,WaterBottle,Account
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth

# Create your views here.

#I hereby attest to the truth of the following facts:
#- I have not discussed the <programming language used> language code in my program
# with anyone other than my instructor or the teaching assistants assigned to this course.
# - I have not used <programming language used> language code obtained from another
# student, or any other unauthorized source, either modified or unmodified.
# - If any <programming language used> language code or documentation used in my
# program was obtained from another source, such as a text book or course notes, that has
# been clearly noted with a proper citation in the comments of my program. 

# Create your views here.

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
            return redirect('view_supplier')
        else:
            messages.info(request,'Invalid credentials for login')
            return redirect('login')
    else:
        return render(request,'Myinventoryapp/login.html')

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
            messages.info(request,'Account created successfully')
            return redirect('login')
            
    else:
        return render(request, 'Myinventoryapp/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def manage_account(request,pk):
    a = get_object_or_404(Account, pk=pk)
    return render(request, 'Myinventoryapp/manage_account.html', {'a': a,})

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
            request.session['password'] = cur
            return redirect('manage_account', pk=pk )

    else:
        u = get_object_or_404(Account,pk=pk)
        return render(request, 'Myinventoryapp/change.html', {'u':u, 'pass':request.session['password']})

def delete_user(request,pk):
    usermodel = Account.objects.get(pk=pk)
    User.objects.filter(username=usermodel.username).delete()
    usermodel.delete()
    auth.logout(request)
    return redirect('login')

def view_supplier(request):
    supplierobjects = Supplier.objects.all()
    accounts = Account.objects.all()
    return render(request, 'Myinventoryapp/supplier.html', {'supplier':supplierobjects, 'accounts':accounts, 'user': request.session['user'],'pass':request.session['password']})

def view_bottles(request):
    bottleobjects = WaterBottle.objects.all()
    return render(request, 'Myinventoryapp/waterbottle.html', {'waterbottle':bottleobjects, 'user': request.session['user']})

def add_bottle(request):
    if (request.method=='POST'):
        brandname = request.POST.get('oname')
        skuname = request.POST.get('snum')
        costname = request.POST.get('cost')
        sizename = request.POST.get('sizenum')
        colorname = request.POST.get('cname')
        quantityname = request.POST.get('qname')
        mouthname = request.POST.get('mouthname')
        suppliername = request.POST.get('supplyname')
        WaterBottle.objects.create(Brand=brandname, SKU=skuname, Cost=costname, Size=sizename, Color=colorname, CurrentQuantity=quantityname, MouthSize=mouthname, Suppliedby=suppliername )
        return redirect('view_bottles')
    else:
        u = Supplier.objects.all()
        return render(request, 'Myinventoryapp/add.html', {'supplier':u, 'user':request.session['user']})

def view_normal(request):
    return render(request, 'Myinventoryapp/view_menu.html', {'user': request.session['user']})

def view_details(request,pk):
    o = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'Myinventoryapp/details.html', {'o':o, 'user': request.session['user']})

def update_bottle(request,pk):
    if (request.method=='POST'):
        brandname = request.POST.get('oname')
        skuname = request.POST.get('snum')
        costname = request.POST.get('cost')
        sizename = request.POST.get('sizenum')
        colorname = request.POST.get('cname')
        quantityname = request.POST.get('qname')
        mouthname = request.POST.get('mouthname')
        suppliername = request.POST.get('supplyname')
        WaterBottle.objects.filter(pk=pk).update(Brand=brandname, SKU=skuname, Cost=costname, Size=sizename, Color=colorname, CurrentQuantity=quantityname, MouthSize=mouthname, Suppliedby=suppliername )
        return redirect('view_bottles')
    else:
        u = Supplier.objects.all()
        o = get_object_or_404(WaterBottle, pk=pk)
        return render(request, 'Myinventoryapp/update_bottle.html', {'o':o, 'supplier':u, 'user': request.session['user']})

def delete_bottle(request,pk):
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles')