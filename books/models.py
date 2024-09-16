from django.db import models


class Book(models.Model):
    GENRE_CHOICES = (
        ('Fantasy', 'Fantasy'),
        ('History', 'History'),
        ('Romance', 'Romance'),
        ('Thriller', 'Thriller'),
    )

    title = models.CharField(max_length=255, verbose_name='Enter book title')
    image = models.ImageField(upload_to='books/', verbose_name='Upload book cover image')
    author = models.CharField(max_length=255, verbose_name='Enter author name')
    description = models.TextField(verbose_name='Write a description of the book')
    price = models.IntegerField(verbose_name='Enter price', null=True)
    publication_year = models.IntegerField(verbose_name='Enter year of publication')
    pages = models.IntegerField(verbose_name='Enter number of pages')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, verbose_name='Select genre')
    url = models.URLField(verbose_name='Enter book URL')
    email = models.EmailField(verbose_name='Enter email for inquiries')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}  "{self.title}" '


class ReviewBook(models.Model):
    book_review = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_book')
    text_book = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text_book} - {self.created_at}'
