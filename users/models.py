from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
   
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=10, validators=[
        MaxValueValidator(99),
        MinValueValidator(5)
    ])
    gender = models.CharField(max_length=10, choices=GENDER)
    developer_level = models.CharField(max_length=10, default='Уровень не определен', null=True, blank=True)
    salary = models.IntegerField(default=0)


@receiver(post_save, sender=CustomUser)
def set_salary(sender, instance, created, **kwargs):
    if created:

        print("Сигнал обработан, пользователь создан")
        level = instance.developer_level
        if level == 'Junior':
            instance.salary = 500
        elif level == 'Middle':
            instance.salary = 1000
        elif level == 'Senior':
            instance.salary = 3000
        else:
            instance.salary = 0
        instance.save()
