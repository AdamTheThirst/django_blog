from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from core import models as core_models


# Create your models here.

class Post(core_models.TimeStampedModel):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Slug')
    body = models.TextField(verbose_name='Основной текст')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='Статус публикации')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',
                               related_name='blog_posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']

        indexes = [
            models.Index(fields=['-publish'])
        ]

