from django.urls import path
from .views import UserList


urlpatterns = [
    path('user_list/', UserList.as_view(), name='user_list')
]