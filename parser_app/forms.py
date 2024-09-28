from django import forms
from . import models, rezka_parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka.ag', 'rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']

    def parser_data(self):
        if self.cleaned_data['media_type'] == 'rezka.ag':
            rezka_films = rezka_parser.parsing()  # Call your parsing function
            for film in rezka_films:
                models.ParserRezka.objects.create(**film)  # Create entries in the database
