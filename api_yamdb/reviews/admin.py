from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_display_links = ('username',)
    readonly_fields = (
        'confirmation_code',
        'last_login',
        'date_joined',
        'is_superuser'
    )
