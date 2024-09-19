from django.urls import path
from . import views

urlpatterns = [
    path('aboutme/', views.about_me),
    path('aboutmyfriend/', views.about_my_friend),
    path('thistime/', views.this_time),

    path('book_list/', views.BookListView.as_view()),
    path('book_list/<int:id>/', views.BookDetailView.as_view()),
    path('create_book/', views.BookCreateView.as_view(), name='add_book'),
    path('book_list/<int:id>/update/', views.BookEditView.as_view()),
    path('book_list_edit/', views.BookUpdateListView.as_view(), name='book_list_edit'),
    path('book_list/<int:id>/delete/', views.BookDropDeleteView.as_view()),
    path('book_list_delete/', views.BookListDeleteView.as_view(), name='book_list_delete'),
    path('search/', views.SearchView.as_view(), name='search'),
]
