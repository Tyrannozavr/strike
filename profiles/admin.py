from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    pass


class RequestsAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Requests, RequestsAdmin)
