from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import User


class UserList(ListView):
    model = User

    def get_queryset(self):
        if self.request:
            username = self.request.GET.get('username')
            return User.objects.filter(username__contains=username)
        return super().get_queryset()



