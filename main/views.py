from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'main/index.html', {"is_main": True})


def sign_up(request):
    return render(request, 'main/sign_up.html', {"is_main": False})

def sign_in(request):
    return render(request, 'main/sign_in.html', {"is_main": False})

def personal_area_main(request):
    return render(request, 'main/personal_area.html', {'is_main': False,
                                                       'chosen': 1})

def personal_area_edit_info(request):
    return render(request, 'main/personal_area_edit_info.html', {'is_main': False, 
                                                                 'chosen': 2})

def personal_area_send_report(request):
    return render(request, 'main/personal_area_send_report.html', {'is_main': False, 
                                                                 'chosen': 3})

def personal_area_log(request):
    return render(request, 'main/personal_area_log.html', {'is_main': False, 
                                                           'chosen': 4})

def check_sign_up(request):
    pass