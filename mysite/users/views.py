from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('/')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Debugging: print username and password to check if they are received
        print(f"Trying to authenticate with username: {username}, password: {password}")

        # Authenticate user with provided credentials
        user = authenticate(request, username=username, password=password)

        # Debugging: check the authenticate result
        print(f"Authenticate result: {user}")

        if user is not None:
            if user.is_active:  # Ensure the user is active
                login(request, user)  # Log the user in
                messages.success(request, 'Logged in successfully!')
                return redirect('home')  # Redirect to home/dashboard page
            else:
                messages.error(request, 'Your account is disabled. Please contact support.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


from django.shortcuts import render, redirect
from .forms import BloodRequestForm
from .models import BloodRequest

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
