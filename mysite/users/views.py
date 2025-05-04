from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from django.shortcuts import render, redirect
from .forms import UserForm, UpdateForm
from .forms import BloodRequestForm
from .models import BloodRequest

@auth
def blood_request_view(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloodreq')  # this name must match your url name
    # Redirect to the same page after POST
    else:
        form = BloodRequestForm()

    blood_requests = BloodRequest.objects.order_by('-requested_at')
    return render(request, 'bloodreq.html', {'form': form, 'blood_requests': blood_requests})



@guest
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'name':'','username':'','blood_group':'','email':'','location':'','phonenumber':'','password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'signup.html',{'form':form})




@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'login.html',{'form':form})

@auth
def dashboard_view(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users':users})


def logout_view(request):
    logout(request)
    return redirect('login')



# def create_profile(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')  # Redirect to the product list page after successful creation
#     else:
#         form = UserForm()
#     return render(request, 'create_profile.html', {'form': form})

def create_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'create_profile.html', {'form': form})


def edit_profile(request, id):
    users = User.objects.get(pk=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the product list page after successful update
    else:
        form = UpdateForm(instance=users)
    return render(request, 'create_profile.html', {'form': form})


def search_donors(request):
    donors = User.objects.filter(usertype='Donor')
    return render(request, 'search_donors.html', {'donors': donors})

