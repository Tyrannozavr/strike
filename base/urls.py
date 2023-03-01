from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('matches/', views.matches, name="matches"),
    path('create/', views.create, name="create"),
    path('coliseum/', views.coliseum, name="coliseum"),
    path('open/', views.open, name="open"),
    path('matchmaking/', views.matchmaking, name="matchmaking"),
    path('matchmaking2/', views.matchmaking2, name="matchmaking2"),
    path('matchmaking3/', views.matchmaking3, name="matchmaking3"),
    ]