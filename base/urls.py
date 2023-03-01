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
    path('tournaments/', views.tournaments, name='tournaments'),
    path('tournaments-info/', views.tournaments_info_active, name='tournaments-info-active'),
    path('tournaments-info-matches/', views.tournaments_info_active2, name='tournaments-info-active2'),
    path('tournaments-info-bracket/', views.tournaments_info_active3, name='tournaments-info-active3'),
    path('tournaments-info-old/', views.tournaments_info, name='tournaments-info'),
    path('goods/', views.goods, name="goods"),
    path('skins/', views.skins, name="skins"),
    path('client/', views.client, name="client"),
    path('promo/', views.promo, name="promo"),
    path('blog/', views.blog, name="blog"),
    path('terms/', views.terms, name="terms"),
    path('policy/', views.policy, name="policy"),
    path('steam/', views.steam, name="steam"),
    path('login/', views.login, name="login"),
    path('sign_up/', views.sign_up, name="sign_up")
    ]