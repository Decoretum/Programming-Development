from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Userperson, Product
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    #Product.objects.create(Name = "NanoLaser",Brand = "NanoTechPH", Color = "Blue",Cost = "P5000")
    return render(request, 'Inventory/home.html')

def Products(request):
    P = Product.objects.all()
    return render(request, 'Inventory/products.html',{'P':P})

def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('usern')
        password = request.POST.get('passn')
        first_name = request.POST.get('firstn')
        last_name = request.POST.get('lastn')
        birthday = request.POST.get('birthday1')
        sex = request.POST.get('sexx')
        print(username)

        if User.objects.filter(username = username):
            messages.info(request,"Username is already taken")
            return redirect('Signup')
        else:
            if username == '' or password == '' or first_name == '' or last_name == '' or birthday == '' or sex == '':
                messages.info(request,"Missing Credentials!")
                return redirect('Signup')
                
            else:
                Userinst = User.objects.create_user(username=username, password=password, 
                first_name=first_name, last_name=last_name)

                Userinst.save()

                Userperson.objects.create(
                    username = username,
                    password = password,
                    first_name = first_name,
                    last_name = last_name,
                    birthday = birthday,
                    sex = sex
                )

                messages.info(request,'Account created successfully')
                return redirect('Login')

    else:
        return render(request,'Inventory/signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        checking = authenticate(request, username=username, password=password)
        if checking is not None:
            login(request, checking)
            userobj = get_object_or_404(Userperson, username=username, password=password )
            request.session['user'] = userobj.username
            request.session['userid'] = userobj.pk
            request.session['password'] = userobj.password
            request.session['firstname'] = userobj.first_name
            request.session['lastname'] = userobj.last_name
            request.session['birthday'] = str(userobj.birthday)
            request.session['sex'] = userobj.sex
            return redirect('home')
        else:
            messages.info(request,'Invalid Login Credentials')
            return redirect('Login')

    else:
        return render(request,'Inventory/Login.html')

def Users(request):
    currentuser = Userperson.objects.filter(username = request.session['username'])
    return render(request,'Inventory/users.html',
    {'username' : request.session['user'],
    'userid' : request.session['userid'],
    'password' : request.session['password'],
    'firstname' : request.session['firstname'],
    'lastname' : request.session['lastname'],
    'birthday' : request.session['birthday'],
    'sex' : request.session['sex'],
    'userobj' : currentuser})

def logout(request):
    auth.logout(request)
    return redirect('Login')

    

def Order(request,pk):
    if request.method == "POST":
        pass
    else:
        return render(request,'Inventory/order.html')


    