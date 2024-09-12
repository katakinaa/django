from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book_id': book_id
            }
        )


def book_list_view(request):
    if request.method == "GET":
        book_object = models.Book.objects.all()
        return render(
            request,
            template_name='book_list.html',
            context={
                'book_object': book_object
            }
        )


def about_me(request):
    return HttpResponse('<h1>Меня зовут Алия, мне 19 лет.</h1>')


def about_my_friend(request):
    return HttpResponse('<h1>Мою подругу зовут Рузана, ей 19 лет.</h1>')


def this_time(request):
    return HttpResponse(datetime.now().strftime('<h1>%H:%M:%S</h1>'))
