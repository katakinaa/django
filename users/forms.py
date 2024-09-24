from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    developer_level = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'developer_level'
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
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
