from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
# messages (message.debug, message.info,message.success, warning,error)

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! you can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm() # get reguest
    return render(request, 'users/register.html', {'form' : form})


@login_required # add functionality to an existing function
def profile(request):
    return render(request, 'users/profile.html' )


