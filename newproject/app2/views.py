# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        a = request.POST['firstname']
        b = request.POST['lastname']
        c = request.POST['email']
        d = request.POST['psw']
        e = request.POST['psw-repeat']
        if d == e:
            x = User.objects.create_user(username=a, last_name=b, email=c, password=d)
            x.save();
            return redirect('login')
            print("saved")

        else:
            messages.info(request,"passwords doen't match")
            return redirect('register')
    return render(request, "reg.html")
