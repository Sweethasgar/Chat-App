from django.contrib import admin

from .models import Profile, Friend,Chattmessage

# Register your models here.
admin.site.register([Profile, Friend,Chattmessage] )
