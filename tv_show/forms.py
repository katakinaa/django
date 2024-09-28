from django import forms
from . import models
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Напишите ваш отзыв...'}),
            'rating': forms.Select(attrs={'class': 'form-control'}, choices=[(i, f'{i} звезды') for i in range(1, 6)]),
        }


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = "__all__"