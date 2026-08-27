from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("email", "username","is_active", "is_staff",)
    list_filter = ("is_active", "is_staff",)

