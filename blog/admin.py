from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Post)
class AdminPost(admin.ModelAdmin):


    list_display = [
       'publish',
       'created',
       'updated',
       'title',
       'slug',
       'body',
       'author',
       'status',
    ]

    list_filter = [
        'author',
        'status',
        'publish',
        'created',
        'updated',
    ]

    search_fields = [
        'title',
        'body',
    ]

    prepopulated_fields = { 'slug' : ('title',)}

    raw_id_fields = ['author']

    date_hierarchy = 'publish'

    ordering = ['status', 'publish']