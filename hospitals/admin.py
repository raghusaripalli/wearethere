from django.contrib import admin

from .models import Hospital, History, Staff

admin.site.register([Hospital, History, Staff])
