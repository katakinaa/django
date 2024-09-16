from django.shortcuts import render
from . import models


def cloth_filter_view(request):
    if request.method == 'GET':
        cloth_kid = models.Cloth.objects.filter(tags__name='для детей').order_by('-id')
        cloth_adult = models.Cloth.objects.filter(tags__name='для взрослых').order_by('-id')
        cloth_pensioner = models.Cloth.objects.filter(tags__name='для персионеров').order_by('-id')
        return render(
            request,
            template_name='filter_list.html',
            context={
                'cloth_kid': cloth_kid,
                'cloth_adult': cloth_adult,
                'cloth_pensioner': cloth_pensioner
            }
        )
