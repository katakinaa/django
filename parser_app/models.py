from django.db import models


class ParserRezka(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='rezka/')

    def __str__(self):
        return self.title
