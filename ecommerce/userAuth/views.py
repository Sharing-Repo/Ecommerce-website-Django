from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .RegisterForm import RegistrationForm

def register(request):
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if (forms.is_valid()):
            forms.save()
            return redirect('user:login')
    else:
        forms = UserCreationForm()
    return render(request, 'users/register.html', {'forms':forms})

def userRegistrationForm(request):
    if request.method == 'POST':
        user_register_form = RegistrationForm(request.POST)
        if (user_register_form.is_valid()):
            user_register_form.save()
            return redirect('user:login')
    else:
        user_register_form = RegistrationForm()
    return render(request, 'users/index.html', {'userForm':user_register_form})

def cust_logout(request):
    logout(request)
    return redirect('user:login')
