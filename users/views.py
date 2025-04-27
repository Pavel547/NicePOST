from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm

@login_required
def profile(request):
    if request.method == "POST":
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")
    else:
        pform = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "users/profile.html", {"pform": pform})
