from django.contrib import auth
from django.core.mail import message
from django.shortcuts import render, redirect
from .models import newproject
from .models import chef_foto
from django.shortcuts import render

from .models import chef_foto
from .models import newproject


def function1(request):
    x = newproject.objects.all()
    y = chef_foto.objects.all()
    return render(request, "index.html", {'result': x, 'result2': y})

def login(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        user=auth.authenticate(username=u,password=p)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            message.info(request,"invalid credentials")
            #return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
