from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout


def login_people(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            message = 2
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')


def registation(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        mail = request.POST.get('user_name')
        if User.objects.filter(username=username).exists():
            message = 1
            return render(request, 'login/registration.html', {'message': message})
        else:
            user = User.objects.create_user(username=username, email=mail, password=password)
            return HttpResponseRedirect('/accounts/login/')

    return render(request, 'login/registration.html')


def custom_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
