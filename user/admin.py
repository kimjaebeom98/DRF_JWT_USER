from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdminConfig(UserAdmin):
    model = User
    list_display = ('email', 'id', 'nickname', 'address', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('-date_joined',)

admin.site.register(User, UserAdminConfig)