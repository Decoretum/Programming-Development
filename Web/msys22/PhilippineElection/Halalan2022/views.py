from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Position,Candidate,Userperson, Vote
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import auth, User
from django.template import loader
from django.http import HttpResponse
from django.db.models import Count

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
            messages.info(request,'Invalid credentials for login')
            return redirect('login')
    else:
        return render(request,'Halalan2022/login.html')

def signup(request):
    if (request.method=='POST'):
        username = request.POST.get('usern')
        password = request.POST.get('passn')
        first_name = request.POST.get('firstn')
        last_name = request.POST.get('lastn')
        birthday = request.POST.get('birthday1')
        sex = request.POST.get('sexx')
     
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username is already taken')
            return redirect('signup')
        
        else:
            Userperson.objects.create(username=username,password=password,first_name=first_name,last_name=last_name,birthday=birthday,sex=sex)
            #model creation


            userobject = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
            userobject.save()
            #registration of user object to auth model

            messages.info(request,'Account created successfully')
            return redirect('login')
    else:
        return render(request, 'Halalan2022/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    c = Candidate.objects.all()
    users = Userperson.objects.all()
    v = Vote.objects.all()
    #Presidents
    for cand in v:
        print(cand)
    countleni = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Robredo')).count()
    countping = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Lacson')).count()
    countnob = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Gonzales')).count()
    countisk = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Domagoso')).count()
    countbong = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Marcos')).count()
    
    #Vice
    countkiko = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Pangilinan')).count()
    countsara = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Duterte')).count()
    countrizal = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='David')).count()  
    countlito = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Atienza')).count()
    countwald = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Bello')).count()
    
    #Senator
    countwin = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Gatchalian')).count()
    countdiaz = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Diaz')).count()
    countherb = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Bautista')).count()
    countchel = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Diokno')).count()
    countneri = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Colmenares')).count()
    #neri = Vote.objects.filter(candidate_id=Candidate.objects.get(last_name__contains='Colmenares'))
    return render(request,'Halalan2022/home.html',{'c':c,'countleni':
    countleni, 'countping':countping,'countnob':countnob,'countisk':countisk,'countbong':countbong,
    'countkiko':countkiko,'countsara':countsara,'countrizal':countrizal,'countlito':countlito,'countwald':countwald,
    'countwin':countwin,'countdiaz':countdiaz,'countherb':countherb,'countchel':countchel,'countneri':countneri,
    'c':c,'v':vote,'u':users, 'user':request.session['user'], 'firstname':request.session['firstname'],'lastname':request.session['lastname']
    })
    

def users(request): 
    userknow = Userperson.objects.get(username=request.session['user']) #user object
    users = Userperson.objects.all()
    vote = Vote.objects.all()
    filter = Vote.objects.filter(user_id=userknow)
    templateloader = loader.get_template('Halalan2022/users.html')
    if filter:
        print('yes')
        context={'condition' : 5, 'v':vote,'u':users, 'id':filter, 'user':request.session['user'], 'pass':request.session['password'], 'firstname':request.session['firstname'],'lastname':request.session['lastname'], 'birthday':request.session['birthday']}
        return HttpResponse(templateloader.render(context,request))      
    else: 
        print('no')
        context={'condition' : 10, 'v':vote,'u':users, 'id':filter, 'user':request.session['user'], 'pass':request.session['password'], 'firstname':request.session['firstname'],'lastname':request.session['lastname'], 'birthday':request.session['birthday']}      
        return HttpResponse(templateloader.render(context,request))
    #return render(request,'Halalan2022/users.html')
         
def candidates(request):
    c = Candidate.objects.all()
    v = Vote.objects.all()
    vicepresident = Position.objects.filter(name='Vice President')
    president = Position.objects.filter(name='President')
    senator = Position.objects.filter(name='Senator')
    return render(request,'Halalan2022/candidates.html',{'c':c, 's': senator, 'v':v, 'p':president, 'vp':vicepresident, 'u':users, 'id':filter, 'user':request.session['user'], 'pass':request.session['password'], 'firstname':request.session['firstname'],'lastname':request.session['lastname'], 'birthday':request.session['birthday']})

def vote(request):
    
    u = Userperson.objects.all()
    v = Vote.objects.all()
    userknow = Userperson.objects.get(username=request.session['user']) #user object
    filter = Vote.objects.filter(user_id=userknow)
    if filter:
        print('yes')
        return redirect('youcant')      
    else:     
        return render(request,'Halalan2022/vote.html',{'person':u,'v':v, 'user':request.session['user']})

def votepage(request,pk):
    if (request.method=='POST'):
        pres = request.POST.get('pres')
        commentp = request.POST.get('commentp')
        vice = request.POST.get('vice')
        commentv = request.POST.get('commentv')
        sen = request.POST.get('sen')
        comments = request.POST.get('comments')
        pres0 = pres.split()
        pres1 = pres0[0]
        pres3 = pres0[-1]
        vice0 = vice.split()
        vice1 = vice0[0]
        vice3 = vice0[-1]
        sen0 = sen.split()
        sen1 = sen0[0]
        sen3 = sen0[-1]

        if commentp == '' or commentv == '' or comments == '':
            messages.info(request,'You must add fields for comments')
            return redirect ('votepage', pk=pk)

        else:
            userid = Userperson.objects.get(pk=pk)
            candid = Candidate.objects.get(first_name__contains=pres1,last_name__contains=pres3)
            Vote.objects.create(user_id=userid,candidate_id=candid,comment=commentp)

            
            candid1 = Candidate.objects.get(first_name__contains=vice1,last_name__contains=vice3)
            Vote.objects.create(user_id=userid,candidate_id=candid1,comment=commentv)

            
            candid2 = Candidate.objects.get(first_name__contains=sen1,last_name__contains=sen3)
            Vote.objects.create(user_id=userid,candidate_id=candid2,comment=comments)
            return redirect('home')
    else:
        u = get_object_or_404(Userperson, pk=pk)
        c = Candidate.objects.all()
        president = Position.objects.filter(name='President')
        vicepresident = Position.objects.filter(name='Vice President')
        senator = Position.objects.filter(name='Senator')
        return render(request,'Halalan2022/votepage.html',{'p':u, 'c':c,'pres':president,'vice':vicepresident,'s':senator, 'v':vote,'u':users, 'id':filter, 'user':request.session['user'], 'pass':request.session['password'], 'firstname':request.session['firstname'],'lastname':request.session['lastname'], 'birthday':request.session['birthday']})
        

def youcant(request):
    return render(request,'Halalan2022/youcant.html')


def about(request):
    u = Userperson.objects.all()
    return render(request,'Halalan2022/about.html',{'person':u})

def update(request,pk):
    if (request.method=='POST'):
        username = request.POST.get('user')
        password = request.POST.get('pass')
        first = request.POST.get('first')
        last = request.POST.get('last')
        birthday = request.POST.get('birthday')
        sex = request.POST.get('sex')
        me = Userperson.objects.get(pk=pk)
        mypass = User.objects.get(username=me.username)
        if birthday == '':
            birthday = me.birthday
        Userperson.objects.filter(pk=pk).update(username=username,password=password,first_name=first,last_name=last,birthday=birthday,sex=sex)
        userobj = get_object_or_404(Userperson, username=username,password=password)
        request.session['user'] = userobj.username
        request.session['password'] = userobj.password
        request.session['userid'] = userobj.pk
        request.session['firstname'] = userobj.first_name
        request.session['lastname'] = userobj.last_name
        request.session['birthday'] = str(userobj.birthday)
        request.session['sex'] = userobj.sex
        mypass.set_password(password)
        mypass.save()
        return redirect('users')
    else:
        u = get_object_or_404(Userperson, pk=pk)
        return render(request, 'Halalan2022/update.html', {'person':u, 'user': request.session['user']})

