from django.urls import path
from .views import ParserFormView, RezkaFilmListView

urlpatterns = [
    path('parser/', ParserFormView.as_view(), name='parser_form'),
    path('films/', RezkaFilmListView.as_view(), name='rezka_film_list'),
]