from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
