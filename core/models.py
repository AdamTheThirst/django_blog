from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):

    ''' Time stamps'''

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    class Meta:
        # Не будет записи в базе данных
        abstract = True