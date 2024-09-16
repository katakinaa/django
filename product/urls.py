from django.urls import path
from . import views

urlpatterns = [
    path('for_kid/', views.cloth_filter_view),
    path('for_adult/', views.cloth_filter_view),
    path('for_pensioner/', views.cloth_filter_view),
]