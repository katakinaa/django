from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from . import models, forms


def about_me(request):
    return HttpResponse('<h1>Меня зовут Алия, мне 19 лет.</h1>')


def about_my_friend(request):
    return HttpResponse('<h1>Мою подругу зовут Рузана, ей 19 лет.</h1>')


def this_time(request):
    return HttpResponse(datetime.now().strftime('<h1>%H:%M:%S</h1>'))


@method_decorator(cache_page(60*15), name='dispatch')
class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self):
        return models.Book.objects.prefetch_related('review_book').all()


@method_decorator(cache_page(60*15), name='dispatch')
class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


@method_decorator(cache_page(60*15), name='dispatch')
class BookCreateView(generic.CreateView):
    template_name = 'crud/create_book.html'
    form_class = forms.BookForm

    def get_success_url(self):
        return reverse('books:book_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


@method_decorator(cache_page(60*15), name='dispatch')
class BookUpdateListView(generic.ListView):
    template_name = 'crud/book_list_edit.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


@method_decorator(cache_page(60*15), name='dispatch')
class BookEditView(generic.UpdateView):
    template_name = 'crud/update_book.html'
    form_class = forms.BookForm
    success_url = '/book_list_edit/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


@method_decorator(cache_page(60*15), name='dispatch')
class BookListDeleteView(generic.ListView):
    template_name = 'crud/book_list_delete.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


@method_decorator(cache_page(60*15), name='dispatch')
class BookDropDeleteView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/book_list_delete/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


@method_decorator(cache_page(60*15), name='dispatch')
class SearchView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_object'
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
