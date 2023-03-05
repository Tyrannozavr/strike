from django.db import IntegrityError
from django.db.models import F, Count, When, Value, BooleanField, Case, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from .models import User
from profiles.models import Requests

# MyModel.objects.extra(select={'custom_field': "'some string or expr'"})
# .values('field1', 'field2', 'custom_field')

# def get_user_list(request):
#     if request.GET:
#         user = request.user
#         username = request.GET.get('username')
#         ivents= [1, 2, 3]
#         users = User.objects\
#             .filter(username__contains=username).exclude(id=user.id)\
#             .extra(select={'field': 'id in [1, 2, 3]'})\
#             .values('id', 'username', 'field')
#         users = [i for i in users]
#         for i in users:
#             print(i)
#         # print(users)
#         return render(request, 'profiles/user_list.html', {'user_list': users})

'''
Product.objects\
    .annotate(image_count=Count('images'))\
    .annotate(
    has_image=
    Case(When(image_count=0, then=Value(False)), default=Value(True), output_field=BooleanField())).order_by(
    '-has_image')
'''


class UserList(ListView):
    model = User

    def get_queryset(self):
        if self.request:
            username = self.request.GET.get('username')
            user = self.request.user
            invites = [i[0] for i in user.sender.all().values_list('recipient')]
            users = User.objects.filter(username__contains=username) \
                .exclude(id=self.request.user.id) \
                .annotate(invited=Case(When(Q(id__in=invites), then=Value(False)), default=Value(True), output_field=BooleanField()))

            for i in users:
                print(i.invited)
            return users
        return super().get_queryset()


from time import time


def profile_friends(request, pk):
    if request.user.is_authenticated:
        # print('user')
        user = User.objects.get(id=pk)
        # print('user', user)
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
            Requests.objects.create(recipient=recipient, inviter=inviter)
            return HttpResponse(status=201)
        except IntegrityError:
            return HttpResponse(status=400)
