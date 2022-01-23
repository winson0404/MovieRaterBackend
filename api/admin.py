from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Movie, Review


class CustomUserAdmin(UserAdmin):
    model = User


admin.site.register(User, CustomUserAdmin)
admin.site.register(Movie)
admin.site.register(Review)
