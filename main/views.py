from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html', {"is_main": True})


def sign_up(request):
    return render(request, 'main/sign_up.html', {"is_main": False})


def sign_in(request):
    return render(request, 'main/sign_in.html', {"is_main": False})

def personal_area(request):
    return render(request, 'main/personal_area.html', {'is_main': False})