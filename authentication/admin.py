from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser


class CustomUsersAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email']

admin.site.register(CustomUser, CustomUsersAdmin)
admin.site.unregister(Group)
# Register your models here.
