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