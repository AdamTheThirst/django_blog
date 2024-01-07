from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
from users.models import User

# admin.site.register(User, CustomUserAdmin)

@admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):
class CustomUserAdmin(UserAdmin):

    """" Custom user admin """

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
    )
    # list_filter = UserAdmin.list_filter + ('superhost',)
    fieldsets = UserAdmin.fieldsets + (
        (
            'Дополнительные поля',
            {
                'fields': (
                    'avatar',
                    'gender',
                    'bio',
                    'birthday',
                    'language',
                )
            }
        ),
    )