from django.shortcuts import render, redirect
from .models import food_items 
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    sat = food_items.objects.all()
    return render(request,'index.html',{'sat':sat})

def register(request):
    if request.method == 'POST':
        username= request.POST['Username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'name not available')
                return redirect('/register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                messages.info(request,'user created')
                return redirect('/mainpage')

        else:
            messages.info(request,'pas not same')
            return redirect('/register')
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username= request.POST['username']
        passwor= request.POST['password']

        user= auth.authenticate(request,username=username,password=passwor)

        if user is not None:
            auth.login(request,user)
            return redirect('/mainpage')
        else:
            messages.info(request,'invaled user')
            return redirect('/login/')
    else:
        return render(request,'login.html')