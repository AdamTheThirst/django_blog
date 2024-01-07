from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    """ Custom model user """

    CHOISES_GENDER = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
    )

    LANG_CHOISE = (
        ('En', 'English'),
        ('Ru', 'Русский'),

    )


    avatar = models.ImageField(verbose_name='Аватар', blank=True, upload_to='avatars')
    gender = models.CharField(max_length=20, verbose_name='Пол', choices=CHOISES_GENDER, blank=True)
    bio = models.TextField(default='', verbose_name='Биография', blank=True)
    birthday = models.DateField(blank=True, verbose_name='Дата рождения', null=True)
    language = models.CharField(max_length=2, default='Ru', verbose_name='Язык')

