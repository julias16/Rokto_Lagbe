from django.shortcuts import render
from users.models import User


def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def bloodreq(request):
    return render(request, 'bloodreq.html')

def searchdonors(request):
    users = User.objects.all()
    return render(request, 'searchdonors.html', {'users': users})
