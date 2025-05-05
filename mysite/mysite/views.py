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

def different_blood_groups(request):
    return render(request, 'different blood groups.html')

def different_blood_terms(request):
    return render(request, 'different blood terms.html')

def how_often_can_i_donate_blood(request):
    return render(request, 'how-often-can-i-donate-blood.html')

def what_is_blood(request):
    return render(request, 'what-is-blood.html')

def what_is_blood_donation(request):
    return render(request, 'what-is-blood-donation.html')

def who_can_donate_blood(request):
    return render(request, 'who-can-donate-blood.html')