from django.shortcuts import render, redirect

from . import models
from .forms import PostForm

def home_view(request):
    posts = models.Post.objects.all()
    return render(request, "nicepostapp/index.html", {'post_list': posts})

def post_details_view(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    return render(request, "nicepostapp/post_detail.html", {'post': post})

def createpost_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nicepost:home')
    else:
        form = PostForm()
    return render(request, "posts/post_form.html", {'createpostform': form})
        