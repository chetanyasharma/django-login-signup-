from django.contrib import admin
from login.models import UserProfile




# Register your models here.
# Update the registeration to include this customised interface
admin.site.register(UserProfile)
