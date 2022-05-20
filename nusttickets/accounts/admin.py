from django.contrib import admin
from .models import User_Account,User_Event

# Register your models here.
admin.site.register(User_Account)
admin.site.register(User_Event)
