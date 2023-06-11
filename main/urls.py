from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'), 
    path('personal_area', views.personal_area_main, name='area1'), 
    path('edit_info', views.personal_area_edit_info, name='area2'), 
    path('send_report', views.personal_area_send_report, name='area3'), 
    path('log', views.personal_area_log, name='area4'), 
    path('personal_area_quit', views.personal_area_quit, name='area_quit')
]
