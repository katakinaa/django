from django.urls import path
from . import views

urlpatterns = [
    path('aboutme/', views.about_me),
    path('aboutmyfriend/', views.about_my_friend),
    path('thistime/', views.this_time),
]
