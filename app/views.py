import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    msg_init = os.listdir(path='/Users/kxrxll/Documents/GitHub/dj-first/app')
    msg = ''
    for item in msg_init:
        msg += item
        msg += '<br>'
    return HttpResponse(msg)
