from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def about_me(request):
    return HttpResponse('<h1>Меня зовут Алия, мне 19 лет.</h1>')


def about_my_friend(request):
    return HttpResponse('<h1>Мою подругу зовут Рузана, ей 19 лет.</h1>')


def this_time(request):
    return HttpResponse(datetime.now().strftime('<h1>%H:%M:%S</h1>'))
