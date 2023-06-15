from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth import models as django_models
from .forms import *
from .models import *
from datetime import datetime, timedelta
from .health_handler import health_rating_handler

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
            
            user = django_models.User.objects.create_user(username=form.data["email"], password=form.data["password"])
            login(request, user)
            user_info = UserInfo(username=form.data["email"])
            user_info.save()
            return redirect('area2')
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
    user_info = UserInfo.objects.get(username=request.user.username)
    medical_info = MedicalInfo.objects.filter(username=request.user.username)

    pulse_array = []
    rating_array = []
    d = {}
    for report in medical_info:
        d[datetime(year=report.report_datetime.year, month=report.report_datetime.month, day=report.report_datetime.day).date()] = report
    
    date = (datetime.today() - timedelta(days=6)).date()
    
    for i in range(7):
        
        if date in d.keys():
            pulse_array.append([i, d[date].pulse1, d[date].pulse2, f"{date.day}.{date.month}"])
            rating_array.append([i, d[date].rating, f"{date.day}.{date.month}"])
        else:
            pulse_array.append([i, 0, 0, f"{date.day}.{date.month}"])
            rating_array.append([i, -1, f"{date.day}.{date.month}"])
        date += timedelta(days=1)

    

    return render(request, 'main/personal_area.html', {'is_main': False, 
                                                       'chosen': 1, 
                                                       "title": get_title(request), 
                                                       "gender": "мужской" if not user_info.gender else "женский", 
                                                       "birth_date": str(user_info.birth_date), 
                                                       "weight": user_info.weight, 
                                                       "message": user_info.message, 
                                                       "pulse_array": pulse_array, 
                                                       "rating_array": rating_array})

def personal_area_edit_info(request):
    if request.method == "POST":
        form = EditInfoForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.data["name"]
            second_name = form.data["second_name"]
            last_name = form.data["last_name"]
            user.first_name = name
            user.last_name = second_name
            user.email = last_name
            user.save()

            gender = form.data["gender"]
            
            birth_date = form.data["birth_date"]
            weight = form.data["weight"]
            user_info = UserInfo.objects.get(username=request.user.username)
            user_info.gender = False if gender == 'Мужской' else True
            if birth_date:
                user_info.birth_date = str(birth_date)
            if weight:
                user_info.weight = weight
            user_info.save()

            
            
            return redirect('area1') 
    else:
        form = EditInfoForm()

    user_info = UserInfo.objects.get(username=request.user.username)

    return render(request, 'main/personal_area_edit_info.html', {'is_main': False, 
                                                                 'chosen': 2, 
                                                                 "title": get_title(request), 
                                                                 "form": form, 
                                                                 "user": request.user, 
                                                                 "weight": user_info.weight, 
                                                                 "birth_date": str(user_info.birth_date), 
                                                                 "gender": user_info.gender})


def check_date(date):
    if datetime.today().year == date.year and datetime.today().month == date.month and datetime.today().day == date.day:
        return True
    return False


def personal_area_send_report(request):
    error = ''
    if request.method == "POST":
        form = ReportForm(request.POST)
        
        if form.is_valid():
            medical_info = MedicalInfo.objects.filter(username=request.user.username)
            if False: #medical_info.exists() and check_date(MedicalInfo.objects.filter(username=request.user.username).order_by("-report_datetime")[0].report_datetime):
                error = 'Вы уже заполняли отчет сегодня!'
            else:
                pulse1 = int(form.data["pulse1"])
                pulse2 = int(form.data["pulse2"])
                preassure1 = int(form.data["preassure1"])
                preassure2 = int(form.data["preassure2"])
                preassure3 = int(form.data["preassure3"])
                preassure4 = int(form.data["preassure4"])
                if pulse1 and pulse2 and preassure1 and preassure2 and preassure3 and preassure4:
                    medical_info = MedicalInfo.objects.filter(username=request.user.username)
                    user_info = UserInfo.objects.get(username=request.user.username)

                    birth_date = user_info.birth_date
                    today = date.today()
                    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                    print(age)
                    if not medical_info.exists():
                        pulse_prev = 60
                    else:
                        last_report = medical_info.order_by("-report_datetime")[0]
                        pulse_prev = (last_report.pulse1 + last_report.pulse2) / 2

                    all_hratings = [report.rating for report in medical_info]
                    
                    [message, hrating] = health_rating_handler(age, pulse1, pulse2, pulse_prev, preassure1, preassure2, preassure3, preassure4, all_hratings)
                    

                    user_info.message = message
                    user_info.save()
                    Report = MedicalInfo(username=request.user.username, 
                                        pulse1=pulse1, pulse2=pulse2,
                                        preassure1=preassure1, preassure2=preassure2, 
                                        preassure3=preassure3, preassure4=preassure4, 
                                        report_datetime=datetime.now(), rating=hrating)
                    Report.save()
                    
                    return redirect('area1')
                else:
                    error = 'Заполните все данные!'
        else:
            error = 'Форма некорректна!'
    else:
        form = ReportForm()
    return render(request, 'main/personal_area_send_report.html', {'is_main': False, 
                                                                 'chosen': 3, 
                                                                 "title": get_title(request), 
                                                                 "form": form, 
                                                                 "error": error, 
                                                                 "datetime": datetime.now()})

def personal_area_log(request):
    reports = MedicalInfo.objects.filter(username=request.user.username).order_by("-report_datetime")
    return render(request, 'main/personal_area_log.html', {'is_main': False, 
                                                           'chosen': 4, 
                                                           "title": get_title(request), 
                                                           "reports": reports})

def personal_area_quit(request):
    logout(request)
    return render(request, 'main/index.html', {"is_main": True, 
                                               "title": get_title(request)})