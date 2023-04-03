from django.contrib import admin
from .models import User
from django.contrib.auth.models import AbstractUser
# Register your models here.
admin.site.register(User)
