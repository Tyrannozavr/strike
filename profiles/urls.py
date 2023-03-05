from django.urls import path
from .views import *


urlpatterns = [
    path('user_list/', UserList.as_view(), name='user_list'),
    path('friends/<str:pk>/', profile_friends, name="friends"),
    path('requests/<str:pk>/', profile_requests, name="requests"),
    path('subscribers/<str:pk>/', profile_subscribers, name="subscribers"),
    path('subscriptions/<str:pk>/', profile_subscriptions, name="subscriptions"),
    path('blocked/<str:pk>/', profile_block, name="block"),
    path('invite_friend/', invite_friend, name='invite_friend')
]