from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list_view),
    path('book_list/<int:id>/', views.book_detail_view),
    path('aboutme/', views.about_me),
    path('aboutmyfriend/', views.about_my_friend),
    path('thistime/', views.this_time),
]
