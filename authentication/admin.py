from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser

#Class to display the fields in the admin page
class CustomUsersAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email']

#Register the User model
admin.site.register(CustomUser, CustomUsersAdmin)

#Unregister the Group class
admin.site.unregister(Group)
