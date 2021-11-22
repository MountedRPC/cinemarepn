from django.contrib import admin
from .models import *
# Register your models here.
from django.conf.urls import url
from django.contrib import admin
from .views import Homepage
from user_profile.models import *

admin.site.register(Films)
admin.site.register(Session)
admin.site.register(Cinemas)
admin.site.register(Sales)