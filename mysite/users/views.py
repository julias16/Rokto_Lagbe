from django.shortcuts import render, redirect
from .forms import UserForm


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('/')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})




