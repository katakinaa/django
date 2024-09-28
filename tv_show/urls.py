from django.urls import path
from . import views

urlpatterns = [
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie_detail/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('create/', views.MovieCreateView.as_view(), name='add_movie'),
    path('update/<int:id>/', views.MovieUpdateView.as_view(), name='edit_movie'),
    path('delete/<int:id>/', views.MovieDeleteView.as_view(), name='delete_movie'),
]
