from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, models, get_user_model
from .forms import *


def get_title(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        second_name = request.user.last_name
        mail = request.user.username
        if first_name:
            return f"{first_name} {second_name}" if second_name else first_name
        else:
            return mail
    else:
        return ''


def index(request):
    return render(request, 'main/index.html', {"is_main": True, 
                                               "title": get_title(request)})


def sign_up(request):
    error = ''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            users = User.objects.all()
            for user in users:
                if user.username == form.data["email"]:
                    error = 'Пользователь уже существует!'
                    return render(request, 'main/sign_up.html', {"is_main": False, 
                                                                 "error": error,
                                                                 "form": SignUpForm(), 
                                                                 "title": get_title(request)})
            if form.data["password"] != form.data["password_check"]:
                error = 'Пароли должны совпадать!'
                return render(request, 'main/sign_up.html', {"is_main": False, 
                                                                 "error": error,
                                                                 "form": SignUpForm(), 
                                                                 "title": get_title(request)})
            
            user = models.User.objects.create_user(username=form.data["email"], password=form.data["password"])
            login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'main/sign_up.html', {"is_main": False, 
                                                 "error": error,
                                                 "form": form, 
                                                 "title": get_title(request)})

def sign_in(request):
    error = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.data["email"], password=form.data["password"])
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                error = "Неверная эл. почта или пароль!"
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {"is_main": False, 
                                               "form": form, 
                                               "error": error, 
                                               "title": get_title(request)})

def personal_area_main(request):
    return render(request, 'main/personal_area.html', {'is_main': False,
                                                       'chosen': 1, 
                                                       "title": get_title(request)})

def personal_area_edit_info(request):
    return render(request, 'main/personal_area_edit_info.html', {'is_main': False, 
                                                                 'chosen': 2, 
                                                                 "title": get_title(request)})

def personal_area_send_report(request):
    return render(request, 'main/personal_area_send_report.html', {'is_main': False, 
                                                                 'chosen': 3, 
                                                                 "title": get_title(request)})

def personal_area_log(request):
    return render(request, 'main/personal_area_log.html', {'is_main': False, 
                                                           'chosen': 4, 
                                                           "title": get_title(request)})

def personal_area_quit(request):
    logout(request)
    return render(request, 'main/index.html', {"is_main": True, 
                                               "title": get_title(request)})