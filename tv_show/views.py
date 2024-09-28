from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView

from . import models, forms
from django.urls import reverse_lazy

from .forms import ReviewForm
from .models import Movie, Review


class MovieListView(ListView):
    template_name = 'movie_list.html'
    context_object_name = 'movies'
    model = models.Movie

    def get_queryset(self):
        return models.Movie.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_movie_url'] = reverse_lazy('add_movie')
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(Movie, id=movie_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()

        # Получаем все отзывы для данного фильма
        reviews = Review.objects.filter(movie=movie)

        # Вычисляем среднюю оценку
        if reviews.exists():
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        else:
            avg_rating = 0  # Или None, в зависимости от вашего предпочтения

        context['reviews'] = reviews
        context['avg_rating'] = avg_rating
        context['review_form'] = ReviewForm()  # Используем импортированную форму
        return context

    def post(self, request, *args, **kwargs):
        movie = self.get_object()
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user if request.user.is_authenticated else None
            review.save()
            return redirect('movie_detail', id=movie.id)

        # Если форма не валидна, возвращаем контекст с ошибками
        context = self.get_context_data()
        context['review_form'] = form
        return self.render_to_response(context)


class MovieCreateView(CreateView):
    model = Movie
    form_class = forms.MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

    def form_valid(self, form):
        return super().form_valid(form)


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = forms.MovieForm
    template_name = 'movie_form.html'
    context_object_name = 'movie'
    success_url = reverse_lazy('movie_list')

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(Movie, id=movie_id)


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    context_object_name = 'movie'
    success_url = reverse_lazy('movie_list')

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(Movie, id=movie_id)
