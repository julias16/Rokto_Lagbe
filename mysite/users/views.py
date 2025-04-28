from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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



# from django.shortcuts import render, redirect
# from .forms import UserForm
#
# def signup_view(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Redirect to the product list page after successful creation
#     else:
#         form = UserForm()
#     return render(request, 'signup.html', {'form': form})




from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
# Create your views here.

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
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')
