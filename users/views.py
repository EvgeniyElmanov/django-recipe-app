from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import forms

# Create your views here.
def register(request):
  if request.method == "POST":
    form = forms.UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"{username}, ваша учетная запись создана, пожалуйста, войдите в систему.")
      return redirect('user-login')
  else:
    form = forms.UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

def custom_logout(request):
  logout(request)
  return redirect('user-login')

@login_required()
def profile(request):
  return render(request, 'users/profile.html')

