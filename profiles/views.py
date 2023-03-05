from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from .models import User
from profiles.models import Requests

class UserList(ListView):
    model = User

    def get_queryset(self):
        if self.request:
            username = self.request.GET.get('username')
            return User.objects.filter(username__contains=username).exclude(id=self.request.user.id)
        return super().get_queryset()


from time import time


def profile_friends(request, pk):
    if request.user.is_authenticated:
        print('user')
        user = User.objects.get(id=pk)
        print('user', user)
        context = {'user': user}
        context['now'] = time()
        return render(request, 'base/profilefriends.html', context)
    else:
        return redirect('login')


def profile_requests(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(id=pk)
        context = {'user': user}
        return render(request, 'base/requests.html', context)
    else:
        return redirect('login')


def profile_subscribers(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(id=pk)
        context = {'user': user}
        return render(request, 'base/subscribers.html', context)
    else:
        return redirect('login')


def profile_subscriptions(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(id=pk)
        context = {'user': user}
        return render(request, 'base/subscriptions.html', context)
    else:
        return redirect('login')


def profile_block(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(id=pk)
        context = {'user': user}
        return render(request, 'base/block.html', context)
    else:
        return redirect('login')


def invite_friend(request):
    if request.GET:
        recipient_id = request.GET.get('inviter_id')
        recipient = User.objects.get(id=recipient_id)
        inviter = request.user
        try:
            Requests.objects.get(inviter=inviter, recipient=recipient)
        except ObjectDoesNotExist:
            print('all right')
            Requests.objects.create(recipient=recipient, inviter=inviter)
            return HttpResponse(status=201)
    return HttpResponse(status=400)

