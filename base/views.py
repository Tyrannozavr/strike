from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def matches(request):
    return render(request, 'base/matches.html')

def create(request):
    return render(request, 'base/create.html')

def coliseum(request):
    return render(request, 'base/coliseum.html')

def open(request):
    return render(request, 'base/open.html')

def matchmaking(request):
    return render(request, 'base/matchmaking.html')
def matchmaking2(request):
    return render(request, 'base/matchmaking2.html')
def matchmaking3(request):
    return render(request, 'base/matchmaking3.html')

def tournaments(request):
    return render(request, 'base/tournaments.html')
def tournaments_info_active(request):
    return render(request, 'base/tournaments-info-active.html')
def tournaments_info_active2(request):
    return render(request, 'base/tournaments-info-active2.html')
def tournaments_info_active3(request):
    return render(request, 'base/tournaments-info-active3.html')
def tournaments_info(request):
    return render(request, 'base/tournaments-info.html')

def goods(request):
    return render(request, 'base/goods.html')

def skins(request):
    return render(request, 'base/skins.html')

def client(request):
    return render(request, 'base/client.html')

def promo(request):
    return render(request, 'base/promo.html')

def blog(request):
    return render(request, 'base/blog.html')

def terms(request):
    return render(request, 'base/terms.html')

def policy(request):
    return render(request, 'base/policy.html')

def steam(request):
    return render(request, 'base/steam.html')

def login(request):
    return render(request, 'base/sign_in.html')

def sign_up(request):
    return render(request, 'base/sign_up.html')