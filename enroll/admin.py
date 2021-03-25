from django.contrib import admin
from .models import User2
# Register your models here.

@admin.register(User2)
class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'password')