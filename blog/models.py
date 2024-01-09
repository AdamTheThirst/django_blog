from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from core import models as core_models


# Create your models here.

# Модельный менеджер - извлекает только опубликованные/неопубликованные посты посты
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.DRAFT)

# Основная таблица
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

    object = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']

        indexes = [
            models.Index(fields=['-publish'])
        ]

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

