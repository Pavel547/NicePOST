from django.shortcuts import render, redirect
from . import models
from .forms import ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profile(request):
    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages("Your profile was update")
            return reversed("profile")
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "pform": profile_form
    }   
    return render(request, "users/profile.html", context)
